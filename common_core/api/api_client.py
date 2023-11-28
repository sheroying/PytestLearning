# from common_core.api.http_util import HttpMethod
# import allure
#
# from conftest import get_env
#
#
# # from multi_rater.services_config.endpoints.multi_rater_endpoints import URL
#
#
# class ApiClient():
#     # def __init__(self, payload=None):
#     #     self.url = QA_URL
#     #     self.payload = payload
#     #     self.service = HttpMethod(self.url, self.payload)
#
#     def __init__(self, custom_url=None, payload=None, env=None, api_token=None, session=None):
#         self.account = None
#         self.payload = payload
#         if env is None and custom_url is None: env = get_env #pytest.env
#         self.env = env
#         self.url = custom_url
#         self.cookies = None
#         self.service = HttpMethod(self.url, self.payload, session)
#
#         # if api_token:
#         #     self.headers = {
#         #         "Content-Type": "application/json",
#         #         "AUTHORIZATION": "Token token={token}".format(token=api_key)
#         #     }
#
#     @allure.step
#     def get_valid_login_cookies(self, username, password):
#         self.cookies = {}
#         # get_login_cookies(self.env, username, password))
#         self.account = {'name': username, 'password': password}
#         return self.cookies
#
#     @allure.step
#     def set_cookies(self, cookies):
#         self.cookies = cookies
