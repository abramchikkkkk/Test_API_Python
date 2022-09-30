import json
from pathlib import PurePath

"""Метод чтения и обновления JSON"""

class Json_Path:
    update_place = PurePath("data", "update_new_place.json")
    create_new_place = PurePath("data", "create_new_place.json")
    delete_place = PurePath("data", "delete_place.json")

class Json_edit:
    @staticmethod
    def json_load(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            text = json.load(f)
            return text

    @staticmethod
    def json_update_place_id(json_file, place_id):
        with open(json_file) as f:
            data = json.load(f)
        data["place_id"] = place_id
        with open(json_file, 'w') as f:
            json.dump(data, f)
