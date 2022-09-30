import allure
from requests import Response
from lib.api import Maps_api
from lib.cheking import Cheking
from lib.json_edit import Json_edit, Json_Path


"""Создание, изменение и удаление новой локации"""
@allure.epic("Test create place")
class Test_place:

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        print("Метод POST")
        result_post: Response = Maps_api.create_new_place()
        chek_post = result_post.json()
        place_id = chek_post.get("place_id")
        print("Place_id : " + place_id)
        Json_edit.json_update_place_id(Json_Path.update_place, place_id)
        Json_edit.json_update_place_id(Json_Path.delete_place, place_id)
        Cheking.chek_status_code(result_post, 200)
        Cheking.chek_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.chek_json_value(result_post, 'status', 'OK')

        print("Метод GET post")
        result_get: Response = Maps_api.get_new_place(place_id)
        Cheking.chek_status_code(result_get, 200)
        Cheking.chek_json_token(result_get,
                                ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                 'language'])
        Cheking.chek_json_value(result_get, 'address', '29,side layout, cohen 09')

        print("Метод PUT")
        result_put: Response = Maps_api.put_new_place()
        Cheking.chek_status_code(result_put, 200)
        Cheking.chek_json_token(result_put, ['msg'])
        Cheking.chek_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET put")
        result_get: Response = Maps_api.get_new_place(place_id)
        Cheking.chek_status_code(result_get, 200)
        Cheking.chek_json_token(result_get,
                                ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                 'language'])
        Cheking.chek_json_value(result_get, 'address', '123 Lenina street, RU')

        print("Метод DELETE")
        result_del: Response = Maps_api.delete_new_place()
        Cheking.chek_status_code(result_del, 200)
        Cheking.chek_json_token(result_del, ['status'])
        Cheking.chek_json_value(result_del, 'status', 'OK')

        print("Метод GET del")
        result_get: Response = Maps_api.get_new_place(place_id)
        Cheking.chek_status_code(result_get, 404)
        Cheking.chek_json_token(result_get, ['msg'])
        Cheking.chek_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
