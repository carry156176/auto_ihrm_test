"""
员工接口
"""
import requests

import app


class EmpApi(object):
    def __init__(self):
        self.add_emp_api = app.BASE_URL + "/api/sys/user"

    # 添加员工
    def add_emp(self, username, mobile, headers):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-05-05",
            "formOfEmployment": 1,
            "departmentName": "测试部",
            "departmentId": "1063678149528784896",
            "correctionTime": "2020-05-30T16:00:00.000Z"
        }
        return requests.post(self.add_emp_api, json=data, headers=headers)

    # 查询员工
    def query_emp(self, emp_id, headers):
        query_url = self.add_emp_api + "/" + emp_id
        return requests.get(query_url, headers=headers)

    # 修改员工
    def put_emp(self, emp_id, data, headers):
        put_url = self.add_emp_api + "/" + emp_id
        return requests.put(put_url, json=data, headers=headers)

    # 删除员工
    def del_emp(self, emp_id, headers):
        del_url = self.add_emp_api + "/" + emp_id
        return requests.delete(del_url, headers=headers)
