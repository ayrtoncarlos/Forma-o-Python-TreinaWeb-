from repositorios import cliente_repositorio
from queries import pedido_query, produto_query
from dominios.db import Pedido


class PedidoRepositorio():
    def inserir_pedido(self, id_cliente, sessao, produtos):
        repositorio_cliente = cliente_repositorio.ClienteRepositorio()
        query_pedido = pedido_query.PedidoQuery()
        query_produto = produto_query.ProdutoQuery()
        cliente = repositorio_cliente.listar_cliente_id(id_cliente, sessao)
        novo_pedido = Pedido(cliente=cliente)
        for p in produtos:
            produto = query_produto.listar_produto_id(p, sessao)
            novo_pedido.produtos.append(produto)
        query_pedido.inserir_pedido(novo_pedido, sessao)
    
    def listar_pedidos(self, sessao):
        query_pedido = pedido_query.PedidoQuery()
        pedidos = query_pedido.listar_pedidos(sessao)
        return pedidos
