from dzcarssalkhim.carss.database import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String(250), nullable=False)
    cars = relationship('Carss')

    def __repr__(self):
        return f"Группа ({self.id}, Название: {self.group_name})"
