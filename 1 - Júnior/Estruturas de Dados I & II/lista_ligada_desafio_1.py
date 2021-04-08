class No():
    def __init__(self, elemento, proximo=None):
        self.__elemento = elemento
        self.__proximo = proximo
    
    @property
    def elemento(self):
        return self.__elemento
    
    @elemento.setter
    def elemento(self, elemento):
        self.__elemento = elemento

    @property
    def proximo(self):
        return self.__proximo
    
    @proximo.setter
    def proximo(self, proximo):
        self.__proximo = proximo


class ListaLigada():
    def __init__(self):
        self.__primeiro_no = None
        self.__ultimo_no = None
        self.__tamanho = 0
    
    def __str__(self):
        temp = self.__primeiro_no
        elementos = ''
        while(temp):
            elementos += f'{temp.elemento} '
            temp = temp.proximo
        return '[' + ','.join([i for i in elementos.strip().split(' ')]) + ']'
    
    def inserir(self, elemento):
        novo_no = No(elemento)
        if self.esta_vazia():
            self.__primeiro_no = novo_no
            self.__ultimo_no = novo_no
        else:
            self.__ultimo_no.proximo = novo_no
            self.__ultimo_no = novo_no
        self.__tamanho += 1
    
    def remover_posicao(self, posicao):
        if posicao == 0:
            proximo_no = self.__primeiro_no.proximo
            self.__primeiro_no = None
            self.__primeiro_no = proximo_no
        elif posicao == self.__tamanho-1:
            penultimo_no = self.recuperar_no(self.__tamanho-2)
            penultimo_no.proximo = None
            self.__ultimo_no = penultimo_no
        else:
            no_remover = self.recuperar_no(posicao)
            no_anterior = self.recuperar_no(posicao-1)
            no_anterior.proximo = no_remover.proximo
            no_remover.proximo = None
        self.__tamanho -= 1
    
    def recuperar_no(self, posicao):
        resultado = 0
        for i in range(posicao+1):
            if i == 0:
                resultado = self.__primeiro_no
            else:
                resultado = resultado.proximo
        return resultado
    
    def esta_vazia(self):
        return self.__tamanho == 0

if __name__ == '__main__':
    inp = [int(i) for i in input().split(',')]
    n = int(input())
    
    lista_ligada = ListaLigada()
    
    for e in inp:
        lista_ligada.inserir(e)
    
    lista_ligada.remover_posicao(n-1)
    print(lista_ligada)
    