import animal, aquatico

class Reptil(animal.Animal, aquatico.Aquatico):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":

    r = Reptil()

    # Exibe o nome das superclasses
    print("Minhas superclasses são: " + str(sorted(r.__class__.__bases__, key = lambda x: x.__name__)))

    r.andar()
    r.nadar()