import datetime
from sqlalchemy import orm
import sqlalchemy
from data.db_session import SqlAlchemyBase
sa = sqlalchemy


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    team_leader = sa.Column(sa.Integer)
    job = sa.Column(sa.String, sa.ForeignKey('users.id'), nullable=True)
    work_size = sa.Column(sa.Integer, nullable=True)
    collaborators = sa.Column(sa.String)
    start_date = sa.Column(sa.Date, nullable=True, default=datetime.datetime.now())
    end_date = sa.Column(sa.Date, nullable=True)
    is_finished = sa.Column(sa.Boolean, index=True)
    team_leader_user = orm.relationship('User')


