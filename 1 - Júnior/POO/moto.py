import veiculo

class Moto(veiculo.Veiculo):
    """Essa é a classe Moto. Essa classe é utilizada para instanciar novas motos em nosso programa. """
    def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiros):
        super().__init__(cor, tipo_combustivel, potencia)
        self.__qtd_passageiros = qtd_passageiros

    def abastecer(self, qtd_combustivel):
        print("Este método foi chamado a partir da classe Moto")
        if self._qtd_combustivel >= 30:
            print("O tanque da moto está cheio!")
        else:
            self._qtd_combustivel += qtd_combustivel
    
    def pintar(self, cor):
        if cor == "azul":
            print("A moto não pode ser azul")
        else:
            self._cor = cor
