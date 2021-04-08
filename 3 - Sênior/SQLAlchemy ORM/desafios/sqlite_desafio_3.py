from sqlalchemy import Table, Column, Integer, String, Date, CHAR
import sqlalchemy as db

engine = db.create_engine('sqlite:///desafio.db')

metadata = db.MetaData()
metadata.reflect(bind=engine)

pessoa = Table('pessoa', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('nome', String(512), nullable=False),
        Column('data_nascimento', Date, nullable=False),
        Column('cpf', CHAR(14), nullable=True)
        )

for t in metadata.sorted_tables:
    print("Table: " + t.name)
    for c in t.primary_key.columns:
        print(f"Primary Key: {c.name} - {c.autoincrement}")
    print("Columns:")
    for c in t._columns:
        print(f'{c.name} - {c.type} - {c.nullable}')
