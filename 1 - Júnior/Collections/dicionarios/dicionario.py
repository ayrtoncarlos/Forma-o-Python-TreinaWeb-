meu_dicionario = {1: 'Thais', 2: 'Ayrton', 3: 'Cristine', 4: 'Felipe'}

print(type(meu_dicionario))
print(meu_dicionario)

outro_dicionario = dict({1: 'Rafaela', 2: 'Mateus', 3: 'Fernanda'})

print(type(outro_dicionario))
print(outro_dicionario)

print(meu_dicionario[2])

for chave, valor in outro_dicionario.items():
    print(f'Chave: {chave} - Valor: {valor}')
