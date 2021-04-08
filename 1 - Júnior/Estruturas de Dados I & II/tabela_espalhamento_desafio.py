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
        elementos = '['
        while(temp):
            elementos += f'{temp.elemento} '
            temp = temp.proximo
        elementos = f'{elementos.strip()}]'
        return elementos
    
    def inserir(self, elemento):
        novo_no = No(elemento)
        if self.esta_vazia():
            self.__primeiro_no = novo_no
            self.__ultimo_no = novo_no
        else:
            self.__ultimo_no.proximo = novo_no
            self.__ultimo_no = novo_no
        self.__tamanho += 1
    
    def inserir_posicao(self, posicao, elemento):
        novo_no = No(elemento)
        if posicao == 0:
            novo_no.proximo = self.__primeiro_no
            self.__primeiro_no = novo_no
        elif posicao == self.__tamanho:
            self.__ultimo_no.proximo = novo_no
            self.__ultimo_no = novo_no
        else:
            no_anterior = self.recuperar_no(posicao-1)
            no_atual = self.recuperar_no(posicao)
            no_anterior.proximo = novo_no
            novo_no.proximo = no_atual
        self.__tamanho += 1
    
    def remover_elemento(self, elemento):
        no_remover = self.indice(elemento)
        if no_remover == -1:
            print('O elemento não existe')
        self.remover_posicao(no_remover)
    
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
    
    def recuperar_elemento_no(self, posicao):
        no = self.recuperar_no(posicao)
        if no != None:
            return no.elemento
        return None
    
    def recuperar_no(self, posicao):
        resultado = 0
        for i in range(posicao+1):
            if i == 0:
                resultado = self.__primeiro_no
            else:
                resultado = resultado.proximo
        return resultado
    
    def contem(self, elemento):
        for i in range(self.__tamanho):
            no_atual = self.recuperar_no(i)
            if no_atual.elemento == elemento:
                return True
        return False

    def indice(self, elemento):
        for i in range(self.__tamanho):
            no_atual = self.recuperar_no(i)
            if no_atual.elemento == elemento:
                return i
        return -1
    
    def esta_vazia(self):
        return self.__tamanho == 0
    
    def tamanho_lista_ligada(self):
        return self.__tamanho


class TabelaEspalhamento():
    def __init__(self):
        self.__elementos = ListaLigada()
        self.__numero_categorias = 10
        self.__tamanho = 0

        for _ in range(self.__numero_categorias):
            self.__elementos.inserir(ListaLigada())
    
    def __str__(self):
        return self.__elementos.__str__()
    
    def __gerar_numero_espalhamento(self, elemento):
        return hash(elemento) % self.__numero_categorias

    def inserir(self, elemento):
        if self.contem(elemento):
            return False
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        categoria.inserir(elemento)
        self.__tamanho += 1
        return True
    
    def remover(self, elemento):
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        categoria.remover_elemento(elemento)
        self.__tamanho -= 1

    def contem(self, elemento):
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        return categoria.contem(elemento)
    
    def tamanho(self):
        return self.__tamanho


class Conjunto():
    def __init__(self):
        self.__elementos = TabelaEspalhamento()
    
    def __str__(self):
        return self.__elementos.__str__()
    
    def inserir(self, elemento):
        self.__elementos.inserir(elemento)
    
    def remover_elemento(self, elemento):
        return self.__elementos.remover(elemento)

    def contem(self, elemento):
        return self.__elementos.contem(elemento)
    
    def esta_vazia(self):
        return self.__elementos.tamanho() == 0
    
    def tamanho_conjunto(self):
        return self.__elementos.tamanho()


if __name__ == '__main__':
    conjunto = Conjunto()
    
    t = int(input())
    
    for _ in range(t):
        names = input()
        conjunto.inserir(names)
        print(conjunto.tamanho_conjunto())
