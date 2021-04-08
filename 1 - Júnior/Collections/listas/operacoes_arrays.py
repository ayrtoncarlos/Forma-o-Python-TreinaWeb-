from array import array

array_1 = array('B', [1, 2, 3, 4, 5, 6])
print(array_1)

for i in array_1:
    print(i)

# Inserindo elementos no array
array_1.insert(2, 50)
print(array_1)

# Removendo elementos do array
array_1.remove(4)
print(array_1)

# Buscar elementos em um array
print(array_1.index(50))

# Atualizar dados em um array
array_1[2] = 55
print(array_1)

array_2 = array('u', ['A', 'E', 'I', 'O', 'U'])
print(' '.join(array_2))
