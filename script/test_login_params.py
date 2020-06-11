import unittest

from parameterized import parameterized

import app
from api.login_api import LoginApi
from utils import assert_text, read_json_data


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()

    @parameterized.expand(read_json_data(app.BASE_DIR + "/data/login_data.json"))
    def test_01login(self, case_name, request_body, success, code, message, http_code):
        json_data = request_body
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(json_data=json_data, headers=headers)

        # 调用断言方法
        assert_text(self, http_code, success, code, message, response)
