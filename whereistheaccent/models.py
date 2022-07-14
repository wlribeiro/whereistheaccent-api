from sqlalchemy import Column, Integer, String, types

from whereistheaccent.db import Base


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String(50))
    is_accented = Column(Integer, default='1')

