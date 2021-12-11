import json
import os

from PIL import Image
import requests


class Greeting:

    all_greeting = []

    def __init__(self, namе, text, url):
        self.name = namе
        self.text = text
        self.url = url
        self.dump_json()
        self.all_greeting.append(self)

    @classmethod
    def obj_greeting(cls, dict_greeting):
        obj = cls(namе=None, text=None)

        for key, val in dict_greeting.items():
            setattr(obj, key, val)
        return obj

    def dump_json(self):
        path = os.path.join(os.getcwd(), 'data', 'all_greeting.json')

        with open(path, 'a') as file:
            json.dump(self.__dict__, file)

    def load_json(self):
        path = os.path.join(os.getcwd(), 'data', 'all_greeting.json')

        with open(path, 'r') as file:
            Greeting.obj_greeting(json.load(file))

    def load_image(self):
        file_name = f'{self.name}.jpg'
        with Image.open(requests.get(self.url, stream=True).raw) as image:
            image.save(os.path.join(os.getcwd(), 'static', file_name))


