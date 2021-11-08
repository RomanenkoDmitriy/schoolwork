# 3. За допомогою фреймворку Flask реалізувати простий сервер, який буде мати два url:
#     - "/" - повертає список повних імен всіх персон (first_name + last_name), у текстовому представленні.
#     - "/person/<int:person_id>" - повертає тектове представлення інформації про одного користувача.
import json

from flask import Flask, render_template

from lesson28 import Person

app = Flask(__name__)


@app.route('/')
def index():
    # persons_list = 4
    return render_template('base.html', persons=Person.list_per, name='List Person')


@app.route('/person/<int:person_id>')
def person_detail(person_id):
    for person in Person.list_per:
        if person.id == person_id:
            return render_template('person.html', person=person, name='Person')