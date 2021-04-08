class Carro():
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
    
    def __hash__(self):
        return hash(self.__marca + self.__modelo)
    
    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.__marca == other.__marca and
            self.__modelo == other.__modelo
        )


if __name__ == '__main__':
    t = int(input())
    
    colecao = set()
    
    for i in range(0, t):
        marca, modelo = input().split()
        colecao.add(Carro(marca, modelo))
        
    print(len(colecao))
