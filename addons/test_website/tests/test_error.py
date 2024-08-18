import sleektiv.tests
from sleektiv.tools import mute_logger


@sleektiv.tests.common.tagged('post_install', '-at_install')
class TestWebsiteError(sleektiv.tests.HttpCase):

    @mute_logger('sleektiv.addons.http_routing.models.ir_http', 'sleektiv.http')
    def test_01_run_test(self):
        self.start_tour("/test_error_view", 'test_error_website')
