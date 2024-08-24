import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = 'inner_man'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Initialize the SQLAlchemy engine using the DATABASE_URL from Config
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

# Optional: Test the connection
try:
    with engine.connect() as connection:
        print("Connection to the database was successful!")
except Exception as e:
    print(f"An error occurred: {e}")
