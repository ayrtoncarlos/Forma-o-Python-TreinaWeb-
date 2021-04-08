tamanho = int(input())
nomes = [input() for _ in range(tamanho)]
nome = input()
index = -1
for idx, name in enumerate(nomes):
    if name == nome:
        index = idx
        break
print(index)
