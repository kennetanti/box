from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hashlib import md5

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(64))
    sessionhash = db.Column(db.String(64), unique=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = md5(password).hexdigest()
        self.sessionhash = md5(username+self.password+email).hexdigest()

    def __repr__(self):
        return '<User %r>' % self.username

    def login(self, password):
        phash = md5(password).hexdigest()
        la = LoginAttempts(self, self.password==phash)
        db.session.add(la)
        db.session.commit()
        if self.password == phash:
            return self.sessionhash
        return "logout"

class LoginAttempts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    success = db.Column(db.Boolean())
    user_id = db.Column(db.Integer(), db.ForeignKey(user.id))
    user = db.relationship('User', backref=db.backref('login_attempts', lazy='dynamic'))
    def __init__(self, user, success):
        self.success = success
        self.user = user
