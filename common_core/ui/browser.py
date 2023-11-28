from common_core.ui.navigation import Navigation
from common_core.ui.selenium_utils import set_up_driver
from common_core.ui.verification import GeneralVerification


class Browser:
    def __init__(self, env=None, temp_path_file=None, driver=None, request=None, driver_type='local'):
        self.env = env
        self.bs_local = None
        if driver:
            self.driver = driver
        else:
            self.driver = set_up_driver(temp_path_file, request=request, session_id=pytest.session_id,
                                        driver_type=driver_type)

        self.navigation = Navigation(self)
        self.verification = GeneralVerification(self)