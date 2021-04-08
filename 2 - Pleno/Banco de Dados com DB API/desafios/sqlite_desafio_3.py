import sqlite3

conn = sqlite3.connect(':memory:')
flag = True

if(conn and isinstance(conn, sqlite3.Connection)):
    print("Conexão realizada!")

    cursor = conn.cursor()

    with conn:
        cursor.execute('''CREATE TABLE IF NOT EXISTS acoes 
                        (data text, trans text, simbolo text, quantidade real, preco real);''')
        

    with conn:
        cursor.execute('''INSERT INTO acoes VALUES 
                        ('2021-03-13', 'COMPRA', 'GOGL34', 100, 190.77), 
                        ('2021-03-13', 'VENDA', 'YAO21', 10, 1.77);''')

    cursor.execute('SELECT COUNT(data) FROM acoes;')

    print(cursor.fetchone()[0])

else:
    flag = False
    print("A conexão não foi realizada!")

conn.close()

if flag:
    print("Conexão finalizada!")
