from sqlalchemy import Boolean, Column, DateTime, Integer, String

from api import db

class Character(db.Model):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    player_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f'<Character {self.name}>'
