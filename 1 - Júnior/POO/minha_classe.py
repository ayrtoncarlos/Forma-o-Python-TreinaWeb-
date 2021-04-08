class MinhaClasse():
    def __del__(self):
        print("Finalizando execução")

if __name__ == "__main__":
    c = MinhaClasse()
    del c