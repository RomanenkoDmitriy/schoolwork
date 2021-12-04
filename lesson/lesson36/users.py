import os
import json
from datetime import datetime


class Posts:

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.date = datetime.date()

    def __lt__(self, other):
        return self.date < other.date


class User:
    list_user = []
    def __init__(self, nickname, password, email):
        self.nickname = nickname
        self.password = password
        self.email = email
        self.img = None
        self.posts = []
        User.list_user.append(self)



    def dump_json(self):
        path = os.path.join(os.getcwd(), 'data', 'users.json')
        with open(path, 'a') as file:
            json.dump(self.__dict__, file)

    def add_posts(self, title, content):
        new_posts = Posts(title, content)
        self.posts.append(new_posts)


# user = User('Bob', 1234, 'qwer')
if __name__ == '__main__':
    user = User('asdas', 345, 'asdfg')
    # user.dump_json()
    user.nickname = 'qwert343'
    print(user.nickname)