import sqlalchemy as db
from sqlalchemy import orm
from sqlalchemy.ext import declarative


Base = declarative.declarative_base()

autor_livro = db.Table('autor_livro', Base.metadata,
                        db.Column('autor_id', db.Integer, db.ForeignKey('autor.id')),
                        db.Column('livro_id', db.Integer, db.ForeignKey('livro.id')))

class Autor(Base):
    __tablename__ = 'autor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(512), nullable=False)
    livros = orm.relationship('Livro', secondary='autor_livro', back_populates='autores')

    def __repr__(self):
        return f"{self.id} {self.nome}"

class Livro(Base):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(512), nullable=False)
    autores = orm.relationship('Autor', secondary='autor_livro', back_populates='livros')

    def __repr__(self):
        return f"{self.nome}"


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
    autores = []
    
    for i in range(t):
        autor_nome = input()
        livro_nome = input()

        novo_livro = Livro(nome=livro_nome)
        
        if autor_nome not in dic.keys():
            dic[autor_nome] = []
            autores.append(autor_nome)
        if not dic[autor_nome].count(novo_livro):
            dic[autor_nome].append(novo_livro)

    for autor in autores:
        novo_autor = Autor(nome=autor)
        for livro in dic[autor]:
            session.add(livro)
            novo_autor.livros.append(livro)
        session.add(novo_autor)
    
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()

try:
    livros = session.query(Livro).options(orm.joinedload(Livro.autores)).order_by(Livro.nome).all()

    nomes_livros = []

    for livro in livros:
        livro.autores.sort(key=lambda x: (x.nome))
        if livro.nome not in nomes_livros:
            print(f"Livro {livro}")
            nomes_livros.append(livro.nome)
        for autor in livro.autores:
            print(autor)

except:
    session.rollback()
    raise
finally:
    session.close()
