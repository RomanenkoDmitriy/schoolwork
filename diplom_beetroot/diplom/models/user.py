import json
import os

class User:
    list_users = []
    def __init__(self, login, _password):
        self.login = login
        self._password = _password
        self.user_hash = hash(self)
        User.list_users.append(self)
        self.id = len(User.list_users)
        self.user_authorization = False

    def __hash__(self):
        return hash((self.login, self._password))

    # def __str__(self):
    #     return f'{self.login}'

    def __repr__(self):
        return f'{self.login}'

    @property
    def password(self):
        return self.user_hash

    def change_login(self, login):
        self.login = login
        self.user_hash = hash(self)

    def change_password(self, password):
        self._password = password
        self.user_hash = hash(self)


class Announcement:

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __str__(self):
        return f'{self.title} {self.text}'

    def dump_json(self, file_name):
        path = os.path.join(os.getcwd(), '..', 'data', f'{file_name}.json')
        with open(path, 'a') as file:
            json.dump(self.__dict__, file)

    @classmethod
    def obj_dict(cls, dict_json):
        obj = cls(title='', text='')
        for key in dict_json:
            setattr(obj, key, dict_json[key])
        return obj

    def load_json(self, login):
        path = os.path.join(os.getcwd(), '..', 'data')
        file_list = os.listdir(path)
        file_name = None
        for file in file_list:
            if file.split('.')[0] == login:
                file_name = file
        file_path = os.path.join(os.getcwd(), '..', 'data', file_name)
        with open(file_path, 'r') as file:
            return Announcement.obj_dict(json.load(file))


user1 = User('qqqq', 1111)
ann = Announcement('test', 'test text')
if __name__ == '__main__':
    user1 = User('qqqq', 1111)
    # print(user1.id)
    # print(user1.password)
    # print(user1.user_hash)
    # print(user1._password)
    # print(user1.login)

    ann = Announcement('test', 'test text')
    # ann.dump_json(user1.login)
    ann1 = ann.load_json(user1.login)
    print(ann1)




    # user1.change_login('wwwwww')
    # print(user1.user_hash)
    # user1.change_password(2222)
    # print(user1.user_hash)

