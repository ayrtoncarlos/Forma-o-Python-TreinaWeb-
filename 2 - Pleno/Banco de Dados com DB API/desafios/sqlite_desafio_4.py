import sqlite3

conn = sqlite3.connect(':memory:')
flag = True

if(conn and isinstance(conn, sqlite3.Connection)):
    print("Conexão realizada!")

    cursor = conn.cursor()

    with conn:
        cursor.execute('''CREATE TABLE acoes 
                        (data text, trans text, simbolo text, quantidade real, preco real);''')

    with conn:
        cursor.execute("INSERT INTO acoes VALUES ('2021-03-14', 'COMPRA', 'APB55', 24, 50.27);")

    cursor.execute('SELECT data, trans, simbolo, quantidade, preco FROM acoes;')

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
        print(f"| {tupla[0]}{' '*(tam[0]-len(str(tupla[0])))} | {tupla[1]}{' '*(tam[1]-len(str(tupla[1])))} | {tupla[2]}{' '*(tam[2]-len(str(tupla[2])))} | {tupla[3]}{' '*(tam[3]-len(str(tupla[3])))} | {tupla[4]}{' '*(tam[4]-len(str(tupla[4])))} |")

else:
    flag = False
    print("A conexão não foi realizada!")

conn.close()

if flag:
    print("Conexão finalizada!")
