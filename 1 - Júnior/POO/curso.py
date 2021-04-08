class Curso():
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def __del__(self):
        print("O objeto foi removido da memória. :)")

if __name__ == "__main__":
    nome = input()
    preco = input()
    descricao = input()

    c = Curso(nome, preco, descricao)

    print(f"Nome: {c.nome} - Preco: {c.preco} - Descrição: {c.descricao}")