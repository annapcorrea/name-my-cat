import sqlalchemy as sa
from app import db

class CatName(db.Model):
    __tablename__ = 'cat_name'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    user_name = db.Column(db.String(64))
    votes = db.Column(db.Integer, default=0)