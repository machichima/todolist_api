import json
from .baseCase import BaseCase

class TestUserLogin(BaseCase):
    def test_successful_login(self):
        username = "paurakh011@gmail.com"
        password = "mycoolpassword"

        payload = json.dumps({
            "username": username,
            "password": password
        })

        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)