import aritmetica

class Sub(aritmetica.Aritmetica):
    def __init__(self, x, y):
        super().__init__(x, y)


if __name__ == "__main__":
    s = Sub()

    # Exibe o nome da superclasse
    print("Minha superclasse é: " + str(s.__class__.__bases__[0]))

    t = int(input())

    for i in range(t):
        x, y = map(int, input().split())
        print(s.subtracao(x, y))