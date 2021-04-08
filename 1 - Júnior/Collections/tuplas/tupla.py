minha_tupla = (1, 2, 3, 4, 5)
outra_tupla = 1, 2, 3, 'Olá', 'Mundo', True, 1.5

print(type(minha_tupla))
print(minha_tupla)

print(type(outra_tupla))
print(outra_tupla)

# count()
print(outra_tupla.count(1))

# index()
print(outra_tupla.index(3))

# Verificar a existencia de um elemento na tupla
print('Olá' in outra_tupla)

# Concatenar tuplas
print(minha_tupla.__add__(outra_tupla))
