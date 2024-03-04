import datetime
import sqlalchemy
from data.db_session import SqlAlchemyBase

sa = sqlalchemy


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    surname = sa.Column(sa.String, nullable=True)
    age = sa.Column(sa.Integer, nullable=True)
    position = sa.Column(sa.String, nullable=True)
    speciality = sa.Column(sa.String, nullable=True)
    address = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, unique=True)
    hashed_password = sa.Column(sa.String, nullable=True, default='1234')
    modified_date = sa.Column(sa.DateTime, default=datetime.datetime.now())
