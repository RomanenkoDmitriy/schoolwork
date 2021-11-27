from flask import Flask, request, render_template, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

from diplom_beetroot.diplom.models.user import User, Announcement, ann
from .utils.authorization import authorization

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data_base/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()


class UserDb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False)
    user_hash = db.Column(db.Integer, nullable=False)
    announcement = db.Column(db.TEXT, nullable=False)
    img_announcement = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<UserDb %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    for user in User.list_users:
        if request.cookies.get(key=user.login):
            # val = request.cookies.values()
            # new_ann = Announcement.load_json(val)
            return render_template('index.html', title=ann.title, text=ann.text)
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
        for user in User.list_users:
            if user.user_hash == hash((login, password)):
                user.add_token()
                # resp = make_response(redirect('/'))
                # resp.set_cookie(key=user.login, value=user.login)
                # return resp
    return render_template('login_user.html')
