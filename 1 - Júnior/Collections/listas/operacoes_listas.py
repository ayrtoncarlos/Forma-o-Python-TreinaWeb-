lista_simples_inteiros = [1, 2, 3, 4, 5]
lista_simples_strings = ['Olá', 'Mundo']
lista_simples_mesclado = [1, 2, 3, 'Olá', 'Mundo', True, 1.5]
nested_list = [[1, 2, True], ['Olá', 'Mundo']]

print(lista_simples_inteiros)
print(nested_list)

# len()
print(len(lista_simples_mesclado))
print(len(nested_list))

# append()
lista_simples_inteiros.append(6)
print(lista_simples_inteiros)

# insert()
#lista_simples_inteiros.insert(2, "Olá")
#print(lista_simples_inteiros)

# remove()
lista_simples_inteiros.remove(1)
print(lista_simples_inteiros)

# index()
#indice = lista_simples_inteiros.index('Olá')
#print(indice)

# count()
lista_simples_inteiros.append(3)
lista_simples_inteiros.append(3)
contagem = lista_simples_inteiros.count(3)
print(lista_simples_inteiros)
print(contagem)

# sort()
lista_simples_inteiros.sort(reverse=True)
print(lista_simples_inteiros)
