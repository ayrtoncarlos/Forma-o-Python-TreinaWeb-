from listas import lista_duplamente_ligada

class Pilha():
    def __init__(self):
        self.__elementos = lista_duplamente_ligada.ListaDuplamenteLigada()
    
    def __str__(self):
        return self.__elementos.__str__()
    
    def empilhar(self, elemento):
        self.__elementos.inserir(elemento)

    def desempilhar(self):
        if self.esta_vazia():
            return None
        resultado = self.__elementos.recuperar_elemento_no(self.tamanho_pilha()-1)
        self.__elementos.remover_posicao(self.tamanho_pilha()-1)
        return resultado

    def topo(self):
        if self.esta_vazia():
            return None
        return self.__elementos.recuperar_elemento_no(self.tamanho_pilha()-1)

    def esta_vazia(self):
        return self.__elementos.esta_vazia()
    
    def tamanho_pilha(self):
        return self.__elementos.tamanho_lista_duplamente_ligada()