import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://Mark:New Pasword@localhost/pitchapp'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # e-mail configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") 
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production config child class

    Args:
        Config: The parent config class with general config classes
    '''
    SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing config child class

    Args:
        Config: The parent config class with General config settings
    '''
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://Mark:New Pasword@localhost/pitchapp'
    