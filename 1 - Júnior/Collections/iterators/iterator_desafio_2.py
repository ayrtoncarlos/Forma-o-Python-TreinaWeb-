class Lista ():
    def __init__(self):
        self.__list = []
 
    def inserir(self, valor):
        self.__list.append(valor)
        
    def iterator(self):
        return iter(self.__list)

if __name__ == "__main__":
    lista = Lista()
    t = int(input())
    
    for i in range(0,t):
        valor = int(input())
        lista.inserir(valor)
        
    lista = lista.iterator()
    
    for valor in lista:
        print(str(valor), end=' ')