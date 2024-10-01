from app import db
from app.models import User
from werkzeug.security import generate_password_hash

def create_user(name,username,email,mno,password,enrolled_mess):
    password_hash = generate_password_hash()