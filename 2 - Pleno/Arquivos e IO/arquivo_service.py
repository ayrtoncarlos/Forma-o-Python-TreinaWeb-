from contato import Contato


def tamanho_campos(lista_contatos):
    max_tamanho_campos = [0, 0, 0]
    for tupla in lista_contatos:
        indice = 0
        nome_contato = tupla.nome
        if len(nome_contato) > max_tamanho_campos[indice]:
            max_tamanho_campos[indice] = len(nome_contato)
        indice += 1
        email_contato = tupla.email
        if len(email_contato) > max_tamanho_campos[indice]:
            max_tamanho_campos[indice] = len(email_contato)
        indice += 1
        telefone_contato = tupla.telefone
        if len(telefone_contato) > max_tamanho_campos[indice]:
            max_tamanho_campos[indice] = len(telefone_contato)
    return max_tamanho_campos

def listar_contatos():
    lista_contatos = list()
    try:
        with open('contatos.txt', 'r') as arquivo:
            listar_contatos_arquivos = arquivo.readlines()
            for c in listar_contatos_arquivos:
                dados = (c.split('-'))
                contato_arquivo = Contato(dados[0][:-1], dados[1][1:-1], dados[2][1:-1])
                lista_contatos.append(contato_arquivo)
        return lista_contatos
    except FileNotFoundError:
        print('Arquivo não encontrado')

def cadastrar_contato(contato_novo):
    try:
        with open('contatos.txt', 'a') as arquivo:
            arquivo.write(f'{contato_novo.nome} - {contato_novo.email} - {contato_novo.telefone}\n')
    except FileNotFoundError:
        print('Arquivo não encontrado')

def buscar_contato(email):
    contatos = listar_contatos()
    for contato in contatos:
        if contato.email == email:
            return contato
    return None

def remover_contato(contato):
    contatos = listar_contatos()
    for c in contatos:
        if c.email == contato.email:
            contatos.remove(c)
            break
    try:
        with open('contatos.txt', 'w') as arquivo:
            for contato in contatos:
                arquivo.write(f'{contato.nome} - {contato.email} - {contato.telefone}\n')
    except FileNotFoundError:
        print('Arquivo não encontrado')
