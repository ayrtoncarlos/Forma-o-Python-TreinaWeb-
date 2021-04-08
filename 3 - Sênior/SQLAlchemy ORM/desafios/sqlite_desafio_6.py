import sqlalchemy as db
import sqlite3
from sqlalchemy import orm
from sqlalchemy.ext import declarative
from datetime import datetime

def lista_pessoas():
    linhas = sqlite3.connect('desafio.db').cursor().execute('SELECT * FROM pessoa').fetchall()
    col_width = [max(len(str(x)) + 2 for x in col) for col in zip(*linhas)]
    for a in linhas:
        print("| {:<{align_col_0}} | {:<{align_col_1}} | {:<{align_col_2}} | {:<{align_col_3}} "
            .format(a[0], a[1], a[2], a[3],
                    align_col_0=col_width[0],
                    align_col_1=col_width[1],
                    align_col_2=col_width[2],
                    align_col_3=col_width[3]))

engine = db.create_engine('sqlite:///desafio.db')

Base = declarative.declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(512), nullable=False)
    data_nascimento = db.Column(db.Date(), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)

    def __repr__(self):
        return "Pessoa %s ('%s', '%s', '%s')" % (self.id, self.nome, self.data_nascimento, self.cpf)

Base.metadata.create_all(engine)

Session = orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

nome = input('Nome: ')
data_nascimento = input('Data de Nascimento (dia/mês/ano): ')
cpf = input('CPF: ')

try:
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
    cliente = Pessoa(nome=nome, data_nascimento=data_nascimento, cpf=cpf)
    session.add(cliente)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()

lista_pessoas()

novo_cpf = input('Novo CPF: ')

try:
    session.query(Pessoa).filter(Pessoa.cpf==cpf).update({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': novo_cpf})
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()

lista_pessoas()
