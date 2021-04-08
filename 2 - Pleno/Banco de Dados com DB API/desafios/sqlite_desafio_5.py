import sqlite3

conn = sqlite3.connect(':memory:')
flag = True

if(conn and isinstance(conn, sqlite3.Connection)):
    print("Conexão realizada!")

    cursor = conn.cursor()

    with conn:
        cursor.execute('''CREATE TABLE acoes 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, trans TEXT, simbolo TEXT, quantidade REAL, preco REAL);''')

    with conn:
        cursor.execute("INSERT INTO acoes (data, trans, simbolo, quantidade, preco) VALUES ('2021-03-15', 'COMPRA', 'APB55', 24, 50.27);")

    cursor.execute('SELECT id, data, trans, simbolo, quantidade, preco FROM acoes;')
    print("Dados atualmente armazenados:")
    print(cursor.fetchall())

    with conn:
        print('\nInsira os dados para alteração:')
        id = input('ID: ')
        trans = input('Trans: ')
        quantidade = input('Quantidade: ')
        cursor.execute("UPDATE acoes SET trans=:trans, quantidade=:quantidade WHERE id=:id", {'trans': trans, 'quantidade': quantidade, 'id': id})

    cursor.execute('SELECT id, data, trans, simbolo, quantidade, preco FROM acoes;')

    dados = cursor.fetchall()
    max_tamanho_campos = [0 for _ in dados[0]]

    for tupla in dados:
        indice = 0
        for dado in tupla:
            if len(str(dado)) > max_tamanho_campos[indice]:
                max_tamanho_campos[indice] = len(str(dado))
            indice += 1
    
    tam = max_tamanho_campos

    for tupla in dados:
        print(f"| {tupla[0]}{' '*(tam[0]-len(str(tupla[0])))} | {tupla[1]}{' '*(tam[1]-len(str(tupla[1])))} | {tupla[2]}{' '*(tam[2]-len(str(tupla[2])))} | {tupla[3]}{' '*(tam[3]-len(str(tupla[3])))} | {tupla[4]}{' '*(tam[4]-len(str(tupla[4])))} | {tupla[5]}{' '*(tam[5]-len(str(tupla[5])))} |")

else:
    flag = False
    print("A conexão não foi realizada!")

conn.close()

if flag:
    print("Conexão finalizada!")
