import unittest

from api.login_api import LoginApi
from utils import assert_text


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()

    def test_01login(self):
        json_data = {"mobile": "13800000002", "password": "123456"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(json_data=json_data, headers=headers)

        # 调用断言方法
        assert_text(self, 200, True, 10000, "操作成功！", response)

    def test_02null_user(self):
        json_data = {"mobile": "", "password": "error"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(json_data=json_data, headers=headers)

        # 调用断言方法
        assert_text(self, 200, False, 20001, "用户名或密码错误", response)

    def test_03null_password(self):
        json_data = {"mobile": "13800000002", "password": "error"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(json_data=json_data, headers=headers)
        print(response.json())

        # 调用断言方法
        assert_text(self, 200, False, 20001, "用户名或密码错误", response)

    def test_04params_null(self):
        json_data = {}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(json_data=json_data, headers=headers)

        # 调用断言方法
        assert_text(self, 200, False, 20001, "用户名或密码错误", response)

    def test_05params_None(self):
        json_data = None
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(json_data=json_data, headers=headers)
        print(response.json())
        # 调用断言方法
        assert_text(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试", response)
