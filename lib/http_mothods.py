import requests
import allure
from lib.logger import Logger

"""Спсок HTTP медодов"""


class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_reqest(url, method="GET")
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_reqest(url, method="POST")
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_reqest(url, method="PUT")
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_reqest(url, method="DELETE")
            result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result
