from flask_app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    deleted = db.Column(db.Integer, default=0)
    active = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<User %r>' % self.username
