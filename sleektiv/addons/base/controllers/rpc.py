import re
import xmlrpc.client
from datetime import date, datetime
from xmlrpc.client import dumps, loads

from werkzeug.wrappers import Response

from sleektiv.http import Controller, dispatch_rpc, request, route
from sleektiv.service import wsgi_server
from sleektiv.fields import Date, Datetime
from sleektiv.tools import lazy, ustr
from sleektiv.tools.misc import frozendict

# ustr decodes as utf-8 or latin1 so we can search for the ASCII bytes
# 	Char	   ::=   	#x9 | #xA | #xD | [#x20-#xD7FF]
XML_INVALID = re.compile(b'[\x00-\x08\x0B\x0C\x0F-\x1F]')
class FlectraMarshaller(xmlrpc.client.Marshaller):
    dispatch = dict(xmlrpc.client.Marshaller.dispatch)

    def dump_frozen_dict(self, value, write):
        value = dict(value)
        self.dump_struct(value, write)
    dispatch[frozendict] = dump_frozen_dict
    
    # By default, in xmlrpc, bytes are converted to xmlrpclib.Binary object.
    # Historically, sleektiv is sending binary as base64 string.
    # In python 3, base64.b64{de,en}code() methods now works on bytes.
    # Convert them to str to have a consistent behavior between python 2 and python 3.
    def dump_bytes(self, value, write):
        # XML 1.0 disallows control characters, check for them immediately to
        # see if this is a "real" binary (rather than base64 or somesuch) and
        # blank it out, otherwise they get embedded in the output and break
        # client-side parsers
        if XML_INVALID.search(value):
            self.dump_unicode('', write)
        else:
            self.dump_unicode(ustr(value), write)
    dispatch[bytes] = dump_bytes

    def dump_datetime(self, value, write):
        # override to marshall as a string for backwards compatibility
        value = Datetime.to_string(value)
        self.dump_unicode(value, write)
    dispatch[datetime] = dump_datetime

    def dump_date(self, value, write):
        value = Date.to_string(value)
        self.dump_unicode(value, write)
    dispatch[date] = dump_date

    def dump_lazy(self, value, write):
        v = value._value
        return self.dispatch[type(v)](self, v, write)
    dispatch[lazy] = dump_lazy


# monkey-patch xmlrpc.client's marshaller
xmlrpc.client.Marshaller = FlectraMarshaller


class RPC(Controller):
    """Handle RPC connections."""

    def _xmlrpc(self, service):
        """Common method to handle an XML-RPC request."""
        data = request.httprequest.get_data()
        params, method = loads(data)
        result = dispatch_rpc(service, method, params)
        return dumps((result,), methodresponse=1, allow_none=False)

    @route("/xmlrpc/<service>", auth="none", methods=["POST"], csrf=False, save_session=False)
    def xmlrpc_1(self, service):
        """XML-RPC service that returns faultCode as strings.

        This entrypoint is historical and non-compliant, but kept for
        backwards-compatibility.
        """
        try:
            response = self._xmlrpc(service)
        except Exception as error:
            response = wsgi_server.xmlrpc_handle_exception_string(error)
        return Response(response=response, mimetype='text/xml')

    @route("/xmlrpc/2/<service>", auth="none", methods=["POST"], csrf=False, save_session=False)
    def xmlrpc_2(self, service):
        """XML-RPC service that returns faultCode as int."""
        try:
            response = self._xmlrpc(service)
        except Exception as error:
            response = wsgi_server.xmlrpc_handle_exception_int(error)
        return Response(response=response, mimetype='text/xml')

    @route('/jsonrpc', type='json', auth="none", save_session=False)
    def jsonrpc(self, service, method, args):
        """ Method used by client APIs to contact OpenERP. """
        return dispatch_rpc(service, method, args)
