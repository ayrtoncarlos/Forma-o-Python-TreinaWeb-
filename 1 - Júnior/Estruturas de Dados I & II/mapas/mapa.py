from listas import lista_ligada
from .associacao import Associacao

class Mapa():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()
        self.__numero_categorias = 10
        self.__tamanho = 0

        for _ in range(self.__numero_categorias):
            self.__elementos.inserir(lista_ligada.ListaLigada())
    
    def __str__(self):
        return self.__elementos.__str__()
    
    def gerar_numero_espalhamento(self, chave):
        return hash(chave) % self.__numero_categorias
    
    def contem_chave(self, chave):
        numero_espalhamento = self.gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        for i in range(categoria.tamanho):
            associacao = categoria.recuperar_elemento_no(i)
            if associacao.chave == chave:
                return True
        return False
    
    def remover(self, chave):
        numero_espalhamento = self.gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        for i in range(categoria.tamanho):
            associacao = categoria.recuperar_elemento_no(i)
            if associacao.chave == chave:
                categoria.remover_elemento(associacao)
                self.__tamanho -= 1
                return True
        return False
    
    def adicionar(self, chave, valor):
        if self.contem_chave(chave):
            self.remover(chave)
        numero_espalhamento = self.gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        categoria.inserir(Associacao(chave, valor))
        self.__tamanho += 1
    
    def recuperar(self, chave):
        numero_espalhamento = self.gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        for i in range(categoria.tamanho):
            associacao = categoria.recuperar_elemento_no(i)
            if associacao.chave == chave:
                return associacao.valor
        return False

    def tamanho_mapa(self):
        return self.__tamanho
