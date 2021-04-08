class Lista ():
    def __init__(self):
        self.__list = []
    
    def __str__(self):
        lista = self.iterator()
        elementos = ''
        while True:
            try:
                elementos += str(next(lista)) + ' '
            except StopIteration:
                break
        return elementos.strip()
        
    def inserir(self, valor):
        self.__list.append(valor)
        
    def iterator(self):
        return iter(self.__list)
        
if __name__ == "__main__":
    lista = Lista()
    
    for item in input().split(' '):
        valor = int(item)
        lista.inserir(valor)
    
    print(lista)