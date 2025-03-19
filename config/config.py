import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Config():
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.urandom(24)
    