from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float

from api import db

clase BaseModel (db.Model):
    id = Column (Integer, primary_key = True)