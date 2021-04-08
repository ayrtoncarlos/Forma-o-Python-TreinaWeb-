from typing import final
import sqlalchemy as db
from sqlalchemy import orm, ForeignKey, Integer
from sqlalchemy.ext import declarative
from sqlalchemy.orm import relationship, joinedload


Base = declarative.declarative_base()

class Jogador(Base):
    __tablename__ = 'jogador'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(512), nullable=False)
    placar = db.Column(db.Integer, nullable=False)
    time_id = db.Column(Integer, ForeignKey('time.id', ondelete="CASCADE"), nullable=False)
    time = relationship('Time', back_populates='jogadores')
    
    def __repr__(self):
        return "- %s %s" % (self.nome, self.placar)

class Time(Base):
    __tablename__ = 'time'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(512), nullable=False)
    jogadores = relationship(
        "Jogador", back_populates="time",
        cascade="all, delete",
        passive_deletes=True
    )

    def __repr__(self):
        return "%s" % (self.nome)

engine = db.create_engine('sqlite:///desafio.db')
Base.metadata.create_all(engine)

for table in Base.metadata.tables:
    print(f"Tabela: {table}")

Session = orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

try:
    t = int(input())

    dic = {}
    times = []

    for i in range(t):
        nome, placar, time_nome = input().split(' ')

        novo_jogador = Jogador(nome=nome, placar=int(placar))
        novo_time = Time(nome=time_nome)         
        
        if time_nome not in dic.keys():
            dic[time_nome] = []
            times.append(time_nome)
        
        dic[time_nome].append(novo_jogador)
        session.add(novo_jogador)

    times.sort()

    for t in times:
        novo_time = Time(nome=t)
        for j in dic[t]:
            novo_time.jogadores.append(j)
        session.add(novo_time)
    
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()

try:
    times = session.query(Time).options(joinedload(Time.jogadores)).order_by(Time.nome).all()
    
    for t in times:
        print(f"Time {t}:")
        t.jogadores.sort(key=lambda x: (x.placar, x.nome), reverse=True)
        for j in t.jogadores:
            print(j)
except:
    session.rollback()
    raise
finally:
    session.close()
