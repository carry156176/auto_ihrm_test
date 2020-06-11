import requests
import app


class LoginApi(object):
    def __init__(self):
        self.login_url = app.BASE_URL + "/api/sys/login"

    def login(self, json_data, headers):
        return requests.post(url=self.login_url, json=json_data, headers=headers)
