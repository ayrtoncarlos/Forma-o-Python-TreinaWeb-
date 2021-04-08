from collections import OrderedDict

class Produto():
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    
    def __str__(self):
        return "{!s} - R${:.2f}".format(self.__nome, self.__preco)
        

if __name__ == "__main__":
    t = int(input())
    
    impars = []
    pares = []
    estoque = {}
    
    for _ in range(t):
        id, nome, preco = [i for i in input().split()]
        
        produto = Produto(nome, float(preco))
        
        if int(id) & 1:
            impars.append([int(id), produto])
        else:
            pares.append([int(id), produto])
    
    impars.sort()
    impars = impars[::-1]
    pares.sort()
    
    for i in impars:
        estoque[i[0]] = i[1]
    
    for i in pares:
        estoque[i[0]] = i[1]
    
    [print("{:d}={!s}".format(k,v)) for k, v in estoque.items()]