from sqlalchemy import Column, String, Boolean, DateTime, Integer

from api import db


class Player(db.Model):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(20), nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False)
    is_admin = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f'<Player {self.first_name} {self.last_name}>'
