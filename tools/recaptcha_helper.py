from flask import request
import requests


class RecaptchaHelper:
    def __init__(self, request):
        self.secret = "6LeB1fAbAAAAAOAbJUG5BJ1utmNn-KVP5UMr2qTS"
        self.request = request

    def validateRecaptcha(self):
        data = {}
        data["secret"] = self.secret
        data["response"] = self.request.form["g-recaptcha-response"]
        response = requests.post(
            "https://www.google.com/recaptcha/api/siteverify", params=data
        )
        if response.status_code == 200:
            messageJson = response.json()
            if messageJson["success"]:
                return True
            else:
                return False
        else:
            return False