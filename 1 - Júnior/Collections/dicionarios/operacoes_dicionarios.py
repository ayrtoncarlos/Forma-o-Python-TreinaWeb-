meu_dicionario = {1: 'Thais', 2: 'Ayrton', 3: 'Cristine', 4: 'Felipe'}

# get()
print(meu_dicionario[2])
print(meu_dicionario.get(2))

# len()
print(len(meu_dicionario))

# pop()
meu_dicionario.pop(4)
print(meu_dicionario)

# keys()
print(meu_dicionario.keys())

# clear()
meu_dicionario.clear()
print(meu_dicionario)

# Adicionando elementos
meu_dicionario[1] = 'Felipe'
print(meu_dicionario)
meu_dicionario.update({'profissao': 'Programador'})
print(meu_dicionario)
