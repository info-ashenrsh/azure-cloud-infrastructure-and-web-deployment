import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "local-development-only-change-this")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///cloudtask.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", "5242880"))
