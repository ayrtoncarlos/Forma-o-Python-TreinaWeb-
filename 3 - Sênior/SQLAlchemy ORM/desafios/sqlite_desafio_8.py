import sqlalchemy as db
from sqlalchemy import orm
from sqlalchemy.ext import declarative


Base = declarative.declarative_base()

class Jogador(Base):
    __tablename__ = 'jogador'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(512), nullable=False)
    placar = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "%s %s" % (self.nome, self.placar)

engine = db.create_engine('sqlite:///desafio.db')

Base.metadata.create_all(engine)

Session = orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

try:
    t = int(input())

    for _ in range(t):
        nome, placar = input().split(' ')
        novo_jogador = Jogador(nome=nome, placar=int(placar))

        session.add(novo_jogador)

    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()

try:
    jogadores = session.query(Jogador).order_by(Jogador.placar.desc(), Jogador.nome).all()

    for j in jogadores:
        print(j) 
except:
    session.rollback()
    raise
finally:
    session.close()
