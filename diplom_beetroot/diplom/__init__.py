import os
from datetime import datetime

from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

from diplom_beetroot.diplom.models.user import User, Announcement, ann
from .utils.authorization import authorization

app = Flask(__name__)
path_db = os.path.abspath(os.path.join(os.getcwd(), 'data_base'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/dimon/schoolwork/diplom_beetroot/diplom/data_base/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class UserDb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False)
    user_hash = db.Column(db.Integer, nullable=False)
    announcement = db.Column(db.TEXT())
    img_announcement = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<UserDb %r>' % self.id


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    # for user in User.list_users:
    #     if request.cookies.get(key=user.login):
    #         # val = request.cookies.values()
    #         # new_ann = Announcement.load_json(val)
    #         return render_template('index.html', title=ann.title, text=ann.text)
    return render_template('index.html', users=User.list_users)


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
        try:
            db.session.add(user_db)
            db.session.commit()
        except Exception as e:
            return render_template('login_user.html', my_eroor=str(e))
        return redirect('/')
    return render_template('login_user.html')
