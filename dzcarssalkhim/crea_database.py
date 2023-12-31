from faker import Faker

from carss.database import create_db, Session
from carss.model import Carss
from carss.group import Group


def crate_database(load_fake_data: object = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    group1 = Group(group_name='A')
    group2 = Group(group_name='B')

    session.add(group1)
    session.add(group2)

    faker = Faker('ru_RU')
    group_list = [group1, group2]
    for _ in range(15):
        model = faker.model().split()
        age = faker.random.randint(2, 15)
        group = faker.random.choice(group_list)

        carss = Carss(model, age, group.id)
    session.commit(carss)
    session.close()


