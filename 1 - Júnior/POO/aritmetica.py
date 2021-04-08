class Aritmetica():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print("O objeto foi removido da memória. :)")

    def subtracao(self, x, y):
        return x - y
