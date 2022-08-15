import json

from requests import Response




"""Методы для проверки ответов наших запросов"""

class Cheking():

    """Метод для проверки статус кода"""
    @staticmethod
    def chek_status_code(respose: Response, status_code):
        # assert status_code == respose.status_code
        if respose.status_code == status_code:
            print("Успешно! Статус код = " + str(respose.status_code))
        else:
            print("Ошибка! Статус код = " + str(respose.status_code))

    """Метод для проверки наличия обязательных полей в ответе запроса"""

    @staticmethod
    def chek_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод для проверки значений обязательных полей в ответе запроса"""

    @staticmethod
    def chek_json_value(response: Response, filde_name, expected_value):
        chek = response.json()
        chek_info = chek.get(filde_name)
        assert chek_info == expected_value
        print(filde_name + " верен!!!")




