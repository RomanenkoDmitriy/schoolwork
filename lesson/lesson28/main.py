# 3. За допомогою фреймворку Flask реалізувати простий сервер, який буде мати два url:
#     - "/" - повертає список повних імен всіх персон (first_name + last_name), у текстовому представленні.
#     - "/person/<int:person_id>" - повертає тектове представлення інформації про одного користувача.
import json

from flask import Flask, render_template, request, jsonify

from lesson28 import Person

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    dict_per = Person.list_per
    if request.method == 'POST':
        dict_per = request.get_json()
        Person.add_person_obj(dict_per)

    return render_template('base.html', persons=dict_per, name='List Person')


@app.route('/person/<int:person_id>')
def person_detail(person_id):
    for person in Person.list_per:
        if person.id == person_id:
            return render_template('person.html', person=person, name='Person')


@app.route('/test', methods=['POST', 'GET', 'PATCH'])
def my_test():
    val = request.get_json(force=True)
    for person in Person.list_per:
        id = int(val['id'])
        if person.id == id:
            person.last_name = val['last_name']
    return val


