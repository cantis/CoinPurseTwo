from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float

from api import db


class BaseModel(db.Model):
    id = Column(Integer, primary_key=True)


class SoftDeleteBaseModel(BaseModel):
    __abstract__ = True

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    deleted_at = Column(DateTime, nullable=True)


class Player(SoftDeleteBaseModel):
    __tablename__ = 'players'

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(20), nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False)
    is_admin = Column(Boolean, nullable=False)

    def __repr__(self):
        return f'<Player {self.first_name} {self.last_name}>'


class Character(SoftDeleteBaseModel):
    __tablename__ = 'characters'

    name = Column(String(50), nullable=False)
    player_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Character {self.name}>'
