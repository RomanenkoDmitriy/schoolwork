import os
import sqlite3
from sqlite3 import Error


class ContextManagerConnect:

    def __init__(self, path):
        self._connect = sqlite3.connect(path)

    def __enter__(self):
        return self._connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connect.close()
        return f'{exc_type}/n{exc_val}/n{exc_tb}'


CREATE_USERS_TABLE = '''CREATE TABLE IF NOT EXISTS user(
                    id integer PRIMARY KEY,
                    first_name text,
                    last_name text NOT NULL
                    );'''
CREATE_USER = '''INSERT INTO user(first_name, last_name) VALUES(?,?)'''
GET_USERS = '''SELECT * FROM user'''

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(str(e))

def create_table(connection, sql_string):
    cursor = connection.cursor()
    cursor.execute(sql_string)

def create_user(connection, sql_string, user_data):
    cursor = connection.cursor()
    cursor.execute(sql_string, user_data)
    connection.commit()

def get_users(connection, sql_string):
    cursor = connection.cursor()
    cursor.execute(sql_string)
    data = cursor.fetchall()
    return data

if __name__ == '__main__':
    database = os.path.join(os.getcwd(), 'mydatabase.db')
    with ContextManagerConnect(database) as connection:
        connection = create_connection(database)
        create_table(connection, CREATE_USERS_TABLE)
        create_user(connection, CREATE_USER, ('Ivan', 'Ivanov'))
        create_user(connection, CREATE_USER, ('Petro', 'Petrov'))
        users = get_users(connection, GET_USERS)
        for user in users:
            print(user)
