from array import array

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
        return elementos.strip()
    
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


class Fila():
    def __init__(self):
        self.__elementos = ListaLigada()

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
    
    def verificar_balanceamento(self):
        pilha = array('u', [])
        cond = True
        indice = 0
        S = array('u', [e for e in self.__str__() if e != ' '])
        
        for i in S:
            if i == '(' or i == '[' or i == '{':
                pilha.insert(0, i)
                indice += 1
            elif i == ')' or i == ']' or i == '}':
                if len(pilha) > 0:
                    if pilha[-1] == chr(ord(i)-1) or pilha[-1] == chr(ord(i)-2):
                        pilha.pop()
                        indice -= 1
                    else:
                        cond = False
                        break
                else:
                    cond = False
                    break
        
        if len(pilha) == 0 and cond: return 'Balanceada'
        return 'Não balanceada'
        
    
    def frente(self):
        if self.esta_vazia():
            return None
        return self.__elementos.recuperar_elemento_no(0)
    
    def tamanho_fila(self):
        return self.__elementos.tamanho_lista_ligada()
    
    def esta_vazia(self):
        return self.__elementos.esta_vazia()


if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        S = input()
        fila = Fila()
        for i in S:
            fila.enfileirar(i)
        print(fila.verificar_balanceamento())
