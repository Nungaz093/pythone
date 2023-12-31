from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
import random
import string
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer)


engine = create_engine('sqlite:///dzalfak.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

from faker import Faker

fake = Faker('ru_RU')

for _ in range(25):
    user = User(name=fake.name(), age=random.randint(18, 50))
    session.add(user)
    session.commit()

for _ in range(25):
    item = Item(name=''.join(random.choices(string.ascii_letters, k=10)),
                user_id=random.randint(1, 50))
    session.add(item)
    session.commit()
