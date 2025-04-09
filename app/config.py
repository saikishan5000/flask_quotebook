import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/quotebook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'super-secret-key')  # used by Flask itself
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-jwt-secret')  # used for JWT
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # optional, in seconds (1 hour)