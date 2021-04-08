import MySQLdb

# CONECTANDO AO BANCO DE DADOS
db = MySQLdb.connect(user='root', passwd='trevas', db='treinaweb_clientes', host='localhost', port=3306, autocommit=False)

print('Conexão realizada com sucesso')

# CRIANDO CURSOR
cursor = db.cursor()

# TRABALHANDO COM TRANSAÇÕES
try:
    db.begin()
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Thais', 26);")
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Fernanda', 28);")
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Cristine', 30);")
    db.commit()
except:
    db.rollback()

# CONSULTANDO DADOS
cursor.execute('SELECT idcliente, nome, idade FROM cliente;')
print(cursor.fetchmany(1))
print(cursor.fetchmany(1))
print(cursor.fetchone())

# INSERINDO MÚLTIPLAS LINHAS COM PARÂMETROS MÚLTIPLOS
try:
    db.begin()
    cursor.executemany("INSERT INTO cliente (nome, idade) VALUES (%s, %s);", 
                        (
                            ('Carlos', 16),
                            ('Cayo', 12),
                            ('Davi', 1),
                            ('Carol', 27),
                        ))
    db.commit()
except:
    db.rollback()

cursor.execute('SELECT idcliente, nome, idade FROM cliente;')
print(cursor.fetchall())

# CONSULTANDO ÚLTIMO ID INSERIDO
print(cursor.lastrowid) # Só está retornando zero
cursor.execute('SELECT LAST_INSERT_ID();') # Esse dá certo
print(cursor.fetchone())

# ATUALIZANDO DADOS
try:
    db.begin()
    cursor.execute("UPDATE cliente SET nome='Felipe' WHERE idcliente=2;")
    db.commit()
except:
    db.rollback()

cursor.execute('SELECT idcliente, nome, idade FROM cliente;')
print(cursor.fetchall())

# REMOVENDO DADOS
try:
    db.begin()
    cursor.execute("DELETE FROM cliente WHERE idcliente=2;")
    db.commit()
except:
    db.rollback()
    
cursor.execute('SELECT idcliente, nome, idade FROM cliente;')
print(cursor.fetchall())

# SQL INJECTION
try:
    db.begin()
    nome = "'Carlos', idade = 80"
    cursor.execute(f"UPDATE cliente SET nome={nome} WHERE idcliente=7;")
    db.commit()
except:
    db.rollback()

cursor.execute('SELECT idcliente, nome, idade FROM cliente;')
print(cursor.fetchall())

# EVITANDO SQL INJECTION COM PARAMETRIZAÇÃO DE CONSULTAS - EXEMPLO 1
try:
    db.begin()
    nome = "'Carlos', idade = 85"
    cursor.execute("UPDATE cliente SET nome=%s WHERE idcliente=7;", (nome, ))
    db.commit()
except:
    db.rollback()

cursor.execute('SELECT idcliente, nome, idade FROM cliente;')
print(cursor.fetchall())

# EVITANDO SQL INJECTION COM PARAMETRIZAÇÃO DE CONSULTAS - EXEMPLO 2
try:
    db.begin()
    nome = "'João', idade = 60"
    cursor.execute("UPDATE cliente SET nome=%(nome)s WHERE idcliente=7;", ({'nome': nome}))
    db.commit()
except:
    db.rollback()

cursor.execute('SELECT idcliente, nome, idade FROM cliente;')
print(cursor.fetchall())

# FINALIZANDO CONEXÃO COM O BANCO DE DADOS
db.close()

print('Conexão finalizada com sucesso')
