from lib.json_edit import Json_edit, Json_Path
from lib.http_mothods import Http_methods

"""Методы для тестирования Maps_api"""

base_url = "https://rahulshettyacademy.com"  # Базовый URL
key = "?key=qaclick123"  # Параметр для всех запросов


class Maps_api:
    """Метод для создания новой локации"""

    @staticmethod
    def create_new_place():
        json_for_create_new_place = Json_edit.json_load(Json_Path.create_new_place)
        post_recource = "/maps/api/place/add/json"
        post_url = base_url + post_recource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):
        get_resourse = "/maps/api/place/get/json"

        get_url = base_url + get_resourse + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для изменения новой локации"""

    @staticmethod
    def put_new_place():
        json_for_update_new_place = Json_edit.json_load(Json_Path.update_place)
        put_recource = "/maps/api/place/update/json"
        put_url = base_url + put_recource + key
        print(put_url)
        result_put = Http_methods.put(put_url, json_for_update_new_place)
        print(result_put.text)
        return result_put

    """Метод для удаления новой локации"""

    @staticmethod
    def delete_new_place():
        del_recource = "/maps/api/place/delete/json"
        del_url = base_url + del_recource + key
        print(del_url)
        json_for_delete_location = Json_edit.json_load(Json_Path.delete_place)
        result_del = Http_methods.delete(del_url, json_for_delete_location)
        print(result_del.text)
        return result_del