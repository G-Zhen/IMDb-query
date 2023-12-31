from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

class Page1Response(db.Model):
    __tablename__ = 'page1_responses'
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.String(100))
    q2 = db.Column(db.String(100))
    q3 = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='responses')