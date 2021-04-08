class Lista ():
    def __init__(self):
        self.__list = []
 
    def inserir(self, valor):
        self.__list.append(valor)
        
    def items(self):
        n = 0
        while n < len(self.__list):
            yield self.__list[n]
            n += 1

if __name__ == "__main__":
    lista = Lista()
    
    for item in input().split():
        valor = int(item)
        lista.inserir(valor)

    for valor in lista.items():
        print(str(valor), end=' ')