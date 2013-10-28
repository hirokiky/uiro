import sqlalchemy as sa
from uiro.db import Base, Session


class MyModel(Base):
    __tablename__ = 'mymodel'
    query = Session.query_property()

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))

    def __init__(self, name):
        self.name = name
