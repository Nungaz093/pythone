from faker import Faker

from shool.clasis.database import create_db, Session
from shool.clasis.group import Group
from shool.clasis.student import Student


def create_database(load_fake_data=True):
    create_db()


def _load_fake_data(session):
    cls1 = Group(group_name='1А')
    cls2 = Group(group_name='1Б')
    cls3 = Group(group_name='1В')

    session.add(cls1)
    session.add(cls2)
    session.add(cls3)

    session.commit()

    faker = Faker('ru_RU')
    group_list = [cls1, cls2, cls3]

    for _ in range(35):
        full_name = faker.name().split()
        age = faker.random.randint(6, 8)
        group = faker.random.choice(group_list)
        student = Student(full_name, age, group.id)
        session.add(student)

    session.commit()
    session.close()
