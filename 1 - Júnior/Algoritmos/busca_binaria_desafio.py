class Produto:
    def __init__(self, id, nome, quantidade):
        self.__id = id
        self.__nome = nome
        self.__quantidade = quantidade
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

if __name__ == '__main__':
    t = int(input())
    produtos = list()
    for _ in range(t):
        id, nome, quantidade = input().split(' ')
        
        produto = Produto(int(id), nome, int(quantidade))
        produtos.append(produto)
    
    for i in range(t):
        indice_menor = i
        for j in range(i+1, t):
            if produtos[i].quantidade < produtos[j].quantidade:
                indice_menor = j
            elif produtos[i].quantidade == produtos[j].quantidade:
                if produtos[i].nome < produtos[j].nome:
                    indice_menor = j
                elif produtos[i].nome == produtos[j].nome:
                    if produtos[i].id < produtos[j].id:
                        indice_menor = j
        temp = produtos[indice_menor]
        produtos[indice_menor] = produtos[i]
        produtos[i] = temp
    
    resultado = -1
    inicio = 0
    meio = 0
    fim = t - 1
    alvo = int(input())
    while inicio <= fim:
        meio = inicio + (fim - inicio) // 2
        if produtos[meio].quantidade > alvo:
            inicio = meio + 1
        elif produtos[meio].quantidade < alvo:
            fim = meio - 1
        else:
            resultado = meio
            break
    if resultado < 0:
        print(resultado)
    else:
        print(produtos[resultado].nome)
