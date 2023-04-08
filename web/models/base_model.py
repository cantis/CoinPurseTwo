from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float

from web import db

clase BaseModel (db.Model):
    id = Column (Integer, primary_key = True)