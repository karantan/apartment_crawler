from apartment_crawler import settings
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def db_connect():
    """Performs database connection using database settings from settings.py.

    Returns sqlalchemy engine instance
    """
    return create_engine(settings.DATABASE)


def create_tables(engine):
    """Creates apartment table."""
    Base.metadata.create_all(engine)


class Apartment(Base):
    """Sqlalchemy apartmant model"""
    __tablename__ = 'apartment'

    id = Column(Integer, primary_key=True)
    name = Column('name', Unicode(100), nullable=True)
    url = Column('url', Unicode(250), nullable=False)
    price = Column('price', Unicode(100), nullable=True)
    created = Column('created', DateTime, default=datetime.utcnow)
