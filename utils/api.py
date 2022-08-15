from utils.http_mothods import http_methods


"""Методы для тестирования Google_maps_api"""


base_url = "https://rahulshettyacademy.com" #Базовый URL
key = "?key=qaclick123"                     #Параметр для всех запросов

class Google_maps_api():

    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
                "location":{
            "lat":-38.383494,
            "lng":33.427362
            }, 'accuracy':50,
            "name":"Frontline house",
            "phone_number":"(+91) 983 893 3937",
            "address":"29,side layout, cohen 09",
            "types":[
            "shoe park",
            "shop"
            ],
            "website":"http://google.com",
            "language":"French-IN"
        }
        post_recource = "/maps/api/place/add/json"  # Ресурс метода POST
        post_url = base_url + post_recource + key
        print(post_url)
        result_post = http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""
    @staticmethod
    def get_new_place(place_id):

        get_resourse = "/maps/api/place/get/json"  # Ресурс метода GET

        get_url = base_url + get_resourse + key + "&place_id=" + place_id
        print(get_url)
        result_get = http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для изменения новой локации"""
    @staticmethod
    def put_new_place(place_id):
        json_for_update_new_place = {
            "place_id": place_id,
        "address": "100 Lenina street, RU",
        "key": "qaclick123"
        }
        put_recource = "/maps/api/place/update/json"  # Ресурс метода PUT
        put_url = base_url + put_recource + key
        print(put_url)
        result_put = http_methods.put(put_url, json_for_update_new_place)
        print(result_put.text)
        return result_put

    """Метод для удаления новой локации"""

    @staticmethod
    def delete_new_place(place_id):
        del_recource = "/maps/api/place/delete/json"
        del_url = base_url + del_recource + key
        print(del_url)
        json_for_delete_location = {
            "place_id": place_id
        }
        result_del = http_methods.delete(del_url, json_for_delete_location)
        print(result_del.text)
        return result_del