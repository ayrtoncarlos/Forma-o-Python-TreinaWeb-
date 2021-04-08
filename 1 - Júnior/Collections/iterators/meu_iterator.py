class MeuIterator():
    def __init__(self, max=0):
        self.__max = max
    
    def __iter__(self):
        self.__n = 0
        return self
    
    def __next__(self):
        if self.__n <= self.__max:
            resultado = 2 ** self.__n
            self.__n += 1
            return resultado
        else:
            raise StopIteration

for i in MeuIterator(5):
    print(i)
