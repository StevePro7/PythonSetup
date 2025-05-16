import os

class Config:
    #SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/app_db")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:@localhost:5432/app_database")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
