import sleektiv.tests
from sleektiv.tools import mute_logger


@sleektiv.tests.common.tagged('post_install', '-at_install')
class TestWebsiteSession(sleektiv.tests.HttpCase):

    def test_01_run_test(self):
        self.start_tour('/', 'test_json_auth')
