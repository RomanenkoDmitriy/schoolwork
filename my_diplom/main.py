from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .model import UserDb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/dimon/schoolwork/my_diplom/data_base/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

@manager.user_loader
def load_user(user_id):
    return UserDb.query.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')
