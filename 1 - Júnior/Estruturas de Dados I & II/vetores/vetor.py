class Vetor():
    def __init__(self, tamanho=1):
        self.__tamanho = tamanho 
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def __str__(self):
        return '[' + ', '.join([str(elemento) for elemento in self.__elementos]) + ']' 
    
    def contem(self, elemento):
        for i in range(self.__tamanho):
            if self.__elementos[i] == elemento:
                return True
        return False
    
    def indice(self, elemento):
        for i in range(self.__tamanho):
            if self.__elementos[i] == elemento:
                return i
        return -1
    
    def inserir_elemento_posicao(self, posicao, elemento):
        vetor_inicio = self.__elementos[:posicao] + [None]
        vetor_final = self.__elementos[posicao:]
        vetor_inicio[posicao] = elemento
        self.__elementos = vetor_inicio + vetor_final
        self.__tamanho += 1
        self.__posicao += 1

    def inserir_elemento_final(self, elemento):
        if self.__posicao >= self.__tamanho:
            self.__elementos = self.__elementos + [None]
            self.__tamanho += 1
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def remover_elemento_indice(self, posicao):
        vetor_inicio = self.__elementos[:posicao]
        elemento = self.__elementos[posicao]
        vetor_final = self.__elementos[posicao+1:]
        self.__elementos = vetor_inicio + vetor_final
        self.__tamanho -= 1
        self.__posicao -= 1
        return elemento

    def remover_elemento(self, elemento):
        indice = self.indice(elemento)
        return self.remover_elemento_indice(indice)
    
    def listar_elemento(self, posicao):
        return self.__elementos[posicao]
    
    def tamanho_vetor(self):
        return self.__tamanho
