from flask import current_app
from datetime import datetime
from time import time 
import jwt 
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60),  nullable = False)
    img_file = db.Column(db.String(20), nullable=False, default = 'default.jpg')
    post = db.relationship('Post', backref='author', lazy = True)

    def get_secret_token(self, expires=216000):
        return jwt.encode({"reset-password": self.username, 'exp': time() + expires }, key = current_app.config['SECRET_KEY'], )
    

    @staticmethod
    def verify_reset_token(token):
      
        try:
            user = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return None
        return User.query.filter_by(username=user['reset-password']).first()
    
    def __repr__(self):
        return f"User ({self.id}, {self.username}, {self.email}, {self.img_file})"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post ('{self.title}', '{self.date_posted} ')"