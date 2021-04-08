from contato import Contato
from arquivo_service import *


print('-'*30)
print(('-'*3) + ' Agenda de Contatos TW ' + ('-'*3))
print('-'*30)

opcao_menu = 1

while (opcao_menu != 0):
    print('1. Listar contatos')
    print('2. Cadastrar contato')
    print('3. Remover contato')
    print('4. Buscar contato')
    print('0. Sair')
    opcao_menu = int(input('Digite a opção desejada: '))

    if opcao_menu == 1:
        contatos = listar_contatos()
        if len(contatos) > 0:
            print('Contatos atualmente registrados:')
            tam = tamanho_campos(contatos)
            for contato in contatos:
                print(f"Nome: {contato.nome}{' '*(tam[0]-len(contato.nome))} | Email: {contato.email}{' '*(tam[1]-len(contato.email))} | Telefone: {contato.telefone}{' '*(tam[2]-len(contato.telefone))}")
        else:
            print('Não há nenhum contato registrado')
    elif opcao_menu == 2:
        nome_contato = input('Digite o nome do contato: ')
        email_contato = input('Digite o email do contato: ')
        telefone_contato = input('Digite o telefone do contato: ')
        contato_novo = Contato(nome_contato, email_contato, telefone_contato)
        cadastrar_contato(contato_novo)
        print('Contato cadastrado com sucesso')
    elif opcao_menu == 3:
        email_remover = input('Digite o email do contato que deseja remover: ')
        contato = buscar_contato(email_remover)
        if contato != None:
            remover_contato(contato)
            print('Contato removido com sucesso')   
        else:
            print('Contato não encontrado')
    elif opcao_menu == 4:
        email_buscar = input('Digite o email do contato que deseja buscar: ')
        contato = buscar_contato(email_buscar)         
        if contato != None:
            print('Contato encontrado')
            print(f'Nome: {contato.nome} | Email: {contato.email} | Telefone: {contato.telefone}')
        else:
            print('Contato não encontrado')
    elif opcao_menu == 0:
        print('Obrigado por usar a agenda de contatos TW')
        break
    else:
        print('Opção inválida')
