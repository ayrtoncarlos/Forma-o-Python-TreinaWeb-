from repositorios import cliente_repositorio, pedido_repositorio, produto_repositorio
from entidades import cliente, produto
from fabricas import fabrica_conexao


loop_principal = True

while loop_principal:
    print(f"{30*'-'} MENU PRINCIPAL {30*'-'}")
    print('1. Cliente')
    print('2. Produtos')
    print('3. Pedidos')
    print('0. Sair')
    print(f"{76*'-'}")

    menu_principal = int(input('Digite a opção desejada: '))
    
    if menu_principal == 1:
        loop_cliente = True

        while loop_cliente:
            print(f"{31*'-'} MENU CLIENTE {31*'-'}")
            print('1. Inserir cliente')
            print('2. Editar cliente')
            print('3. Remover cliente')
            print('4. Listar todos os clientes')
            print('5. Listar cliente por ID')
            print('6. Listar cliente por nome')
            print('7. Listar cliente por nome (Ordenado)')
            print('0. Sair')
            print(f"{76*'-'}")

            menu_cliente = int(input('Digite a opção desejada: '))

            if menu_cliente == 1:
                fabrica = fabrica_conexao.FabricaConexao()
                sessao = fabrica.criar_sessao()
                try:
                    nome_cliente = input('Digite o nome do cliente: ')
                    idade_cliente = int(input('Digite a idade do cliente: '))
                    novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)
                    repositorio = cliente_repositorio.ClienteRepositorio()
                    repositorio.inserir_cliente(novo_cliente, sessao)
                    sessao.commit()
                except:
                    sessao.rollback()
                    raise
                finally:
                    fabrica.desconectar(sessao)
            elif menu_cliente == 2:
                fabrica = fabrica_conexao.FabricaConexao()
                sessao = fabrica.criar_sessao()
                try:
                    id_cliente = int(input('ID do cliente a ser atualizado: '))
                    nome_cliente = input('Digite o nome do cliente: ')
                    idade_cliente = int(input('Digite a idade do cliente: '))
                    novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)
                    repositorio = cliente_repositorio.ClienteRepositorio()
                    repositorio.editar_cliente(id_cliente, novo_cliente, sessao)
                    sessao.commit()
                except:
                    sessao.rollback()
                    raise
                finally:
                    fabrica.desconectar(sessao)
            elif menu_cliente == 3:
                fabrica = fabrica_conexao.FabricaConexao()
                sessao = fabrica.criar_sessao()
                try:
                    id_cliente = int(input('ID do cliente a ser removido: '))
                    repositorio = cliente_repositorio.ClienteRepositorio()
                    repositorio.remover_cliente(id_cliente, sessao)
                    sessao.commit()
                except:
                    sessao.rollback()
                    raise
                finally:
                    fabrica.desconectar(sessao)
            elif menu_cliente == 4:
                fabrica = fabrica_conexao.FabricaConexao()
                sessao = fabrica.criar_sessao()
                try:
                    repositorio = cliente_repositorio.ClienteRepositorio()
                    clientes = repositorio.listar_clientes(sessao)
                    for c in clientes:
                        print(c)
                except:
                    sessao.rollback()
                    raise
                finally:
                    fabrica.desconectar(sessao)
            elif menu_cliente == 5:
                fabrica = fabrica_conexao.FabricaConexao()
                sessao = fabrica.criar_sessao()
                try:
                    id_cliente = int(input('Digite o ID do cliente a ser procurado: '))
                    repositorio = cliente_repositorio.ClienteRepositorio()
                    cliente = repositorio.listar_cliente_id(id_cliente, sessao)
                    print(cliente)
                except:
                    sessao.rollback()
                    raise
                finally:
                    fabrica.desconectar(sessao)
            elif menu_cliente == 6:
                fabrica = fabrica_conexao.FabricaConexao()
                sessao = fabrica.criar_sessao()
                try:
                    nome_cliente = input('Digite o nome do cliente a ser procurado: ')
                    repositorio = cliente_repositorio.ClienteRepositorio()
                    clientes = repositorio.listar_cliente_nome(nome_cliente, sessao)
                    for c in clientes:
                        print(c)
                except:
                    sessao.rollback()
                    raise
                finally:
                    fabrica.desconectar(sessao)
            elif menu_cliente == 7:
                fabrica = fabrica_conexao.FabricaConexao()
                sessao = fabrica.criar_sessao()
                try:
                    nome_cliente = input('Digite o nome do cliente a ser procurado: ')
                    repositorio = cliente_repositorio.ClienteRepositorio()
                    clientes = repositorio.listar_cliente_nome_ordenado(nome_cliente, sessao)
                    for c in clientes:
                        print(c)
                except:
                    sessao.rollback()
                    raise
                finally:
                    fabrica.desconectar(sessao)
            elif menu_cliente == 0:
                print(f"{26*'-'} Saindo do MENU CLIENTE {26*'-'}")
                loop_cliente = False
            else:
                print('Opção inválida.')
    elif menu_principal == 2:
        loop_produtos = True

        while loop_produtos:
            print(f"{30*'-'} MENU PRODUTOS {31*'-'}")
            print('1. Inserir produto')
            print('2. Listar produto por ID')
            print('0. Sair')
            print(f"{76*'-'}")

            menu_produtos = int(input('Digite a opção desejada: '))

            if menu_produtos == 1:
                fabrica = fabrica_conexao.FabricaConexao()
                sessao = fabrica.criar_sessao()
                try:
                    descricao_produto = input('Digite a descrição do produto: ')
                    valor_produto = float(input('Digite o valor do produto: '))
                    novo_produto = produto.Produto(descricao_produto, valor_produto)
                    repositorio = produto_repositorio.ProdutoRepositorio()
                    repositorio.inserir_produto(novo_produto, sessao)
                    sessao.commit()
                except:
                    sessao.rollback()
                    raise
                finally:
                    fabrica.desconectar(sessao)
            elif menu_produtos == 2:
                fabrica = fabrica_conexao.FabricaConexao()
                sessao = fabrica.criar_sessao()
                try:
                    id_produto = int(input('Digite o ID do produto a ser procurado: '))
                    repositorio = produto_repositorio.ProdutoRepositorio()
                    produto = repositorio.listar_produto_id(id_produto, sessao)
                    print(produto)
                except:
                    sessao.rollback()
                    raise
                finally:
                    fabrica.desconectar(sessao)
            elif menu_produtos == 0:
                print(f"{25*'-'} Saindo do MENU PRODUTOS {26*'-'}")
                loop_produtos = False
            else:
                print('Opção inválida.')
    elif menu_principal == 3:
        loop_pedidos = True

        while loop_pedidos:
            print(f"{31*'-'} MENU PEDIDOS {31*'-'}")
            print('1. Inserir pedido')
            print('2. Listar pedidos')
            print('0. Sair')
            print(f"{76*'-'}")

            menu_pedidos = int(input('Digite a opção desejada: '))

            if menu_pedidos == 1:
                fabrica = fabrica_conexao.FabricaConexao()
                sessao = fabrica.criar_sessao()
                try:
                    loop_pedido_produto = True
                    lista_produtos = []

                    while loop_pedido_produto:
                        print('1. Inserir produto')
                        print('0. Voltar')

                        menu_pedido_produto = int(input('Digite a opção desejada: '))

                        if menu_pedido_produto == 1:
                            id_pedido_produto = int(input('Digite o ID do produto deste pedido: '))
                            lista_produtos.append(id_pedido_produto)
                        elif menu_pedido_produto == 0:
                            loop_pedido_produto = False
                        else:
                            print('Opção inválida.')
                    id_cliente = int(input('Digite o ID do cliente a ser relacionado com o novo pedido: '))
                    repositorio = pedido_repositorio.PedidoRepositorio()
                    repositorio.inserir_pedido(id_cliente, sessao, lista_produtos)
                    sessao.commit()
                except:
                    sessao.rollback()
                    raise
                finally:
                    fabrica.desconectar(sessao)
            elif menu_pedidos == 2:
                fabrica = fabrica_conexao.FabricaConexao()
                sessao = fabrica.criar_sessao()
                try:
                    repositorio = pedido_repositorio.PedidoRepositorio()
                    pedidos = repositorio.listar_pedidos(sessao)

                    for p in pedidos:
                        print(p, p.produtos)
                except:
                    sessao.rollback()
                    raise
                finally:
                    fabrica.desconectar(sessao)
            elif menu_pedidos == 0:
                print(f"{26*'-'} Saindo do MENU PEDIDOS {26*'-'}")
                loop_pedidos = False
            else:
                print('Opção inválida.')
    elif menu_principal == 0:
        print('Obrigado por utilizar o nosso sistema.')
        loop_principal = False
    else:
        print('Opção inválida.')
