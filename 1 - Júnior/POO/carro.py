import veiculo

class Carro(veiculo.Veiculo):
    """Essa é a classe Carro. Essa classe é utilizada para instanciar novos carros em nosso programa. """
    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super().__init__(cor, tipo_combustivel, potencia)
        self.__qtd_portas = qtd_portas

    def abastecer(self, qtd_combustivel):
        print("Este método foi chamado a partir da classe Carro")
        self._qtd_combustivel += qtd_combustivel

    def pintar(self, cor):
        if cor == "preto":
            print("O carro não pode ser preto")
        else:
            self._cor = cor
