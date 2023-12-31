import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'carz.db'

engine = sqlalchemy.create_engine(f"sqlite:///{DATABASE_NAME}")
Session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
