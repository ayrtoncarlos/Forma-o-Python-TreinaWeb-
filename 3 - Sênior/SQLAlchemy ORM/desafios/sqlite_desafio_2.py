from sqlalchemy import Column, Integer, String, Date, Numeric
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Numeric


engine = create_engine('sqlite:///desafio.db')

Base = declarative_base()

class Acoes(Base):
    __tablename__ = 'acoes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False)
    transacao = Column(String(50), nullable=False)
    simbolo = Column(String(16), nullable=False)
    empresa = Column(String(256), nullable=True)
    quantidade = Column(Integer, nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)

Base.metadata.create_all(engine)

metadata = MetaData()
metadata.reflect(bind=engine)

for t in metadata.sorted_tables:
    print("Table: " + t.name)
    for c in t.primary_key.columns:
        print(f"Primary Key: {c.name} - {c.autoincrement}")
    print("Columns:")
    for c in t._columns:
        print(f'{c.name} - {c.type} - {c.nullable}')
