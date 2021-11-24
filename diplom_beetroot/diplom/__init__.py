from flask import Flask, request, render_template, make_response, redirect, url_for

from .models.user import User, Announcement
from .utils.authorization import authorization

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    for user in User.list_users:
        if request.cookies.get(key=user.login):
            val = request.cookies.values()
            new_ann = Announcement.load_json(val)
            return render_template('index.html', title=new_ann.title, text=new_ann.text)
    return render_template('index.html', users=User.list_users)

@app.route('/authorization', methods=['GET', 'POST'])
def user_authorization():
    if request.method == 'POST':
        # if request.form['login'] != '' and request.form['password'] != '':
        login = request.form['login']
        password = request.form['password']
        new_user = User(login, password)
        return render_template('authorization.html', val=True)
    return render_template('authorization.html', val=False)

@app.route('/login_user', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        for user in User.list_users:
            if user.user_hash == hash((login, password)):
                resp = make_response(redirect('/'))
                resp.set_cookie(key=user.login, value=user.login)
                return resp
    return render_template('login_user.html')
