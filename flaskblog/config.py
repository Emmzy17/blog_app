import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres://wabmceiasacllf:5dd711cfa3fcdb8eba99b8c8bfdfa4801e2ed62895ae84d23add1bdb5e27552e@ec2-3-225-213-67.compute-1.amazonaws.com:5432/d4nb5qvpbgmuh3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True 
    MAIL_USERNAME = os.getenv('EMAIL_USRNAME')
    MAIL_PASSWORD = os.getenv('EMAIL_PASSWD')
    