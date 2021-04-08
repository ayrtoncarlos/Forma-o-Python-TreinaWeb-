from listas import lista_ligada

class Fila():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()

    def __str__(self):
        return self.__elementos.__str__()
    
    def enfileirar(self, elemento):
        self.__elementos.inserir(elemento)
    
    def desenfileirar(self):
        if self.esta_vazia():
            return None
        resultado = self.__elementos.recuperar_elemento_no(0)
        self.__elementos.remover_posicao(0)
        return resultado
    
    def frente(self):
        if self.esta_vazia():
            return None
        return self.__elementos.recuperar_elemento_no(0)
    
    def tamanho_fila(self):
        return self.__elementos.tamanho_lista_ligada()
    
    def esta_vazia(self):
        return self.__elementos.esta_vazia()
