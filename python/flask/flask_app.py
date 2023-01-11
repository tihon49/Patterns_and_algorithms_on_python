"""Пример:
    
Перед запуском приложения нужно создать БД:
    python3
    from flask_app import db
    db.create_all()

Далее можно создать пользователя:
    from flask_app import User
    test_user = User(name='test_name', password='test_password')
    session = db.session
    session.add(test_user)
    session.commit()
    session.query(User).all()
    
"""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class User(db.Model):
    """user test model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        return f"<user {self.id} : {self.name}>"


@app.route('/')
def index():
    return {'data': 'test'}


if __name__ == '__main__':
    app.run(debug = True)

