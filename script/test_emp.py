import unittest
import logging
import app
from api.emp_api import EmpApi
from api.login_api import LoginApi
from utils import assert_text


class TestEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()
        cls.emp_api = EmpApi()

    def test_01login_suc(self):
        json_data = {"mobile": "13800000002", "password": "123456"}
        headers = {"Content-Type": "application/json"}
        response = self.login_api.login(json_data=json_data, headers=headers)
        token = "Bearer " + response.json().get("data")

        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        logging.info("把headers保存到全局变量为{}".format(app.HEADERS))
        assert_text(self, 200, True, 10000, "操作成功！", response)

    def test_02add_emp(self):
        response = self.emp_api.add_emp("小船儿飘", 15678881787, headers=app.HEADERS)
        print(response.json())

        app.EMP_ID = response.json()["data"]["id"]
        assert_text(self, 200, True, 10000, "操作成功！", response)

    def test_03query_emp(self):
        print(app.EMP_ID)
        print(app.HEADERS)
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        print(response.json())
        assert_text(self, 200, True, 10000, "操作成功！", response)

    def test_04put_emp(self):
        response = self.emp_api.put_emp(app.EMP_ID, {"username": "小船儿"}, app.HEADERS)
        print(response.json())
        assert_text(self, 200, True, 10000, "操作成功！", response)

    def test_05del_emp(self):
        response = self.emp_api.del_emp(app.EMP_ID, app.HEADERS)
        assert_text(self, 200, True, 10000, "操作成功！", response)
