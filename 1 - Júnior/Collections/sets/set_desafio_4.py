class Carro():
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
    
    def __repr__(self):
        return self.__marca + ' - ' + self.__modelo + ' - ' + str(self.__ano)
  
    def __hash__(self):
        return hash(self.__marca + self.__modelo + str(self.__ano))
    
    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.__marca == other.__marca and
            self.__modelo == other.__modelo and
            self.__ano == other.__ano
        )


if __name__ == '__main__':
    t = int(input())
    
    colecao = set()
    
    for i in range(0, t):
        marca, modelo, ano = input().split()
        colecao.add(Carro(marca, modelo, int(ano)))
    
    colecao_ordenada = sorted(colecao, key=str)
    
    for c in colecao_ordenada:
        print(c)
