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
    
    @property
    def tamanho(self):
        return self.__tamanho
    
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


class Associacao():
    def __init__(self, chave, valor):
        self.__chave = chave
        self.__valor = valor
    
    def __str__(self):
        return f'{self.__chave} {self.__valor}'
    
    @property
    def chave(self):
        return self.__chave
    
    @property
    def valor(self):
        return self.__valor


class Mapa():
    def __init__(self):
        self.__elementos = ListaLigada()
        self.__numero_categorias = 10
        self.__tamanho = 0

        for _ in range(self.__numero_categorias):
            self.__elementos.inserir(ListaLigada())
    
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


if __name__ == '__main__':
    mapa = Mapa()
    
    t = int(input())
    
    for _ in range(t):
        nome = input()
        telefone = input()
        mapa.adicionar(nome, telefone)
    
    q = int(input())
    
    for _ in range(q):
        nome = input()
        if mapa.contem_chave(nome):
            print(f'{nome}={mapa.recuperar(nome)}')
        else:
            print('Não achado')
