import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')
allowed_origin = os.getenv('FRONT_URL')

SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_CONNECTION_URI = (f'mysql+pymysql://{user}:{password}'
                           f'@{host}:{port}/{database}')
