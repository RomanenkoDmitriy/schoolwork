from datetime import datetime

from flask_login import UserMixin

from my_diplom.main import db

class UserDb(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False, unique=True)
    user_hash = db.Column(db.Integer, nullable=False)
    announcement = db.Column(db.TEXT())
    img_announcement = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<UserDb %r>' % self.id



