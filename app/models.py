from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'registered_users'
    
    id = db.Column(db.String(500), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mobile_no = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    enrolled_mess = db.Column(db.String(100))

    def __repr__(self):
        return f'<User {self.email}>'
