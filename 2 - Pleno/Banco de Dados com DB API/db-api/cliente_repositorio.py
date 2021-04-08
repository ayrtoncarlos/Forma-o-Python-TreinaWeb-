import fabrica_conexao

class ClienteRepositorio():
    @staticmethod
    def listar_clientes():
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute('SELECT idcliente, nome, idade FROM cliente;')
            print(cursor.fetchall())
        finally:
            fabrica_conexao.FabricaConexao.desconectar(fabrica)

    @staticmethod
    def inserir_cliente(cliente):
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            fabrica.begin()
            cursor = fabrica.cursor()
            cursor.execute("INSERT INTO cliente (nome, idade) VALUES (%s, %s);", 
                            (cliente.nome, cliente.idade))
            fabrica.commit()
        except:
            fabrica.rollback()
        finally:
            fabrica_conexao.FabricaConexao.desconectar(fabrica)

    @staticmethod
    def editar_cliente(id_cliente, cliente):
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            fabrica.begin()
            cursor = fabrica.cursor()
            cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE idcliente=%(id_cliente)s;", 
                            ({'nome': cliente.nome, 'idade': cliente.idade, 'id_cliente': id_cliente}))
            fabrica.commit()
        except:
            fabrica.rollback()
        finally:
            fabrica_conexao.FabricaConexao.desconectar(fabrica)

    @staticmethod
    def remover_cliente(id_cliente):
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            fabrica.begin()
            cursor = fabrica.cursor()
            cursor.execute("DELETE FROM cliente WHERE idcliente=%(id_cliente)s;", 
                            {'id_cliente': id_cliente})
            fabrica.commit()
        except:
            fabrica.rollback()
        finally:
            fabrica_conexao.FabricaConexao.desconectar(fabrica)
