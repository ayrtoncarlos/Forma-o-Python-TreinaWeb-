from abc import ABC, abstractmethod

class NoArvore(ABC):
    def __init__(self, valor, no_esquerdo=None, no_direito=None):
        self.__valor = valor
        self.__no_esquerdo = no_esquerdo
        self.__no_direito = no_direito
    
    def __str__(self):
        return ('[(X)]' if self.__no_esquerdo == None else f'[({self.__no_esquerdo.__str__()})]') + \
            f'[({self.__valor.__str__()})]' + \
                ('[(X)]' if self.__no_direito == None else f'[({self.__no_direito.__str__()})]')
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def no_esquerdo(self):
        return self.__no_esquerdo
    
    @no_esquerdo.setter
    def no_esquerdo(self, no_esquerdo):
        self.__no_esquerdo = no_esquerdo
    
    @property
    def no_direito(self):
        return self.__no_direito
    
    @no_direito.setter
    def no_direito(self, no_direito):
        self.__no_direito = no_direito
    
    @abstractmethod
    def peso(self):
        pass


class NoArvoreInteiro(NoArvore):
    def __init__(self, valor):
        super().__init__(valor)
    
    def peso(self):
        return self.valor


class Arvore():
    def __init__(self, raiz=None):
        self.__raiz = raiz
    
    def __str__(self):
        return '[(X)]' if self.__raiz == None else self.__raiz.__str__()
    
    @property
    def raiz(self):
        return self.__raiz
    
    def inserir_elemento(self, no):
        no.no_direito = None
        no.no_esquerdo = None
        if self.__raiz == None:
            self.__raiz = no
        else:
            self.__inserir(self.__raiz, no)
    
    def __inserir(self, referencia, novo_no):
        if referencia.peso() < novo_no.peso():
            if referencia.no_direito == None:
                referencia.no_direito = novo_no
            else:
                self.__inserir(referencia.no_direito, novo_no)
        else:
            if referencia.no_esquerdo == None:
                referencia.no_esquerdo = novo_no
            else:
                self.__inserir(referencia.no_esquerdo, novo_no)
    
    def buscar(self, no_busca):
        return self.__buscar(self.__raiz, no_busca)

    def __buscar(self, referencia, no_busca):
        if referencia.valor == no_busca.valor:
            return referencia
        else:
            if referencia.peso() < no_busca.peso():
                if referencia.no_direito == None:
                    raise ValueError('Elemento não encontrado')
                else:
                    print('Navegando pela direita do nó', referencia.valor.__str__())
                    return self.__buscar(referencia.no_direito, no_busca)
            else:
                if referencia.no_esquerdo == None:
                    raise ValueError('Elemento não encontrado')
                else:
                    print('Navegando pela esquerda do nó', referencia.valor.__str__())
                    return self.__buscar(referencia.no_esquerdo, no_busca)

    def em_ordem(self):
        self.__em_ordem(self.__raiz)

    def __em_ordem(self, referencia):
        if referencia.no_esquerdo != None:
            self.__em_ordem(referencia.no_esquerdo)
            print(referencia.valor.__str__())
            if referencia.no_direito != None:
                self.__em_ordem(referencia.no_direito)
        else:
            print(referencia.valor.__str__())
            if referencia.no_direito != None:
                self.__em_ordem(referencia.no_direito)
    
    def pre_ordem(self):
        self.__pre_ordem(self.__raiz)
    
    def __pre_ordem(self, referencia):
        print(referencia.valor.__str__())
        if referencia.no_esquerdo != None:
            self.__pre_ordem(referencia.no_esquerdo)
            if referencia.no_direito != None:
                self.__pre_ordem(referencia.no_direito)
        else:
            if referencia.no_direito != None:
                self.__pre_ordem(referencia.no_direito)
    
    def pos_ordem(self):
        self.__pos_ordem(self.__raiz)
    
    def __pos_ordem(self, referencia):
        if referencia.no_esquerdo != None:
            self.__pos_ordem(referencia.no_esquerdo)
            if referencia.no_direito != None:
                self.__pos_ordem(referencia.no_direito)
            print(referencia.valor.__str__())
        else:
            if referencia.no_direito != None:
                self.__pos_ordem(referencia.no_direito)
                print(referencia.valor.__str__())
            else:
                print(referencia.valor.__str__())
    
    def altura(self):
        return self.__altura(self.__raiz)
    
    def __altura(self, referencia):
        if referencia == None:
            return -1
        altura_esquerda = self.__altura(referencia.no_esquerdo)
        altura_direita = self.__altura(referencia.no_direito)
        return (altura_esquerda+1) if altura_esquerda > altura_direita else (altura_direita+1)


if __name__ == '__main__':
    arvore = Arvore()
    
    while True:
        try:
            valor = int(input())
            arvore.inserir_elemento(NoArvoreInteiro(valor))
        except:
            break
    
    arvore.em_ordem()
