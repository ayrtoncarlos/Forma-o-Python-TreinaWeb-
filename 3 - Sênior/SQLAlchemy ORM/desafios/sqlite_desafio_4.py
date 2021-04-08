import sqlalchemy as db
from sqlalchemy import orm

engine = db.create_engine('sqlite:///desafio.db')

Session = orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

print(session.bind)