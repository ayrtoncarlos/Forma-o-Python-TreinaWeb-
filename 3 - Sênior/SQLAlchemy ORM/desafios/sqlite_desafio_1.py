from sqlalchemy import create_engine

engine = create_engine('sqlite:///desafio.db')

print(engine.url)