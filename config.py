import os

class Config:
    uri = os.getenv("DATABASE_URL", "sqlite:///default.db")  # Default to SQLite
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_flaKEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
