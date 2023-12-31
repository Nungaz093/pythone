from dzcarssalkhim.carss.database import Base
import sqlalchemy


class Carss(Base):
    __tablename__ = 'cars'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    model = sqlalchemy.Column(sqlalchemy.String(250), nullable=False)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    group = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('groups.id'))

    def __init__(self, mode, age, id_group):
        self.model = mode[0]
        self.age = age
        self.group = id_group

    def __repr__(self):
        return f"Модель (Модель машины:{self.model}, Возраст:{self.age}, ID Группы:{self.group})"
