import sqlalchemy as db
from sqlalchemy import orm
from sqlalchemy.ext import declarative
from datetime import datetime


Base = declarative.declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(512), nullable=False)
    data_nascimento = db.Column(db.Date(), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    
    def __repr__(self):
        return "- %s | %s | %s" % (self.nome, self.data_nascimento, self.cpf)

engine = db.create_engine('sqlite:///desafio.db')

Base.metadata.create_all(engine)

Session = orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

try:
    t = int(input())

    for _ in range(t):
        nome = input()
        data_nascimento = input()
        cpf = input()

        nova_pessoa = Pessoa(nome=nome, data_nascimento=datetime.strptime(data_nascimento, '%d/%m/%Y'), cpf=cpf)
        session.add(nova_pessoa)

    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()

try:
    data = datetime.strptime('31/12/1999', '%d/%m/%Y')
    pessoas = session.query(Pessoa).where(Pessoa.data_nascimento < data).all()
    
    for p in pessoas:
        print(p)
except:
    session.rollback()
    raise
finally:
    session.close()
