import os

from flask import Flask, request, render_template, redirect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from models.user import User, UserDb

# from .utils.authorization import authorization

app = Flask(__name__)

path_db = os.path.abspath(os.path.join(os.getcwd(), 'data_base'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/dimon/schoolwork/diplom_beetroot/diplom/data_base/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)


# db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    user_db = UserDb.query.all()
    return render_template('index.html', users=User.list_users, user_db=user_db)


@app.route('/authorization', methods=['GET', 'POST'])
def user_authorization():
    if request.method == 'POST':
        # if request.form['login'] != '' and request.form['password'] != '':
        login = request.form['login']
        password = request.form['password']
        new_user = User(login, password)
        new_user.token = True
        return render_template('authorization.html', val=True)
    return render_template('authorization.html', val=False)


@app.route('/login_user', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user_hash = hash((login, password))
        user_db = UserDb(login=login, user_hash=user_hash)
        # new_user = User(login, password)
        try:
            db.session.add(user_db)
            db.session.commit()
        except Exception as e:
            return render_template('login_user.html', my_eroor=str(e))
        return redirect('/')
    return render_template('login_user.html')
