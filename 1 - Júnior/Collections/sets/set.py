# Declaração de um set
meu_set = {1, 2, 3, 4, 5}

print(type(meu_set))
print(meu_set)

outro_set = set([1, 2, 3])

print(type(outro_set))
print(outro_set)

# add()
meu_set.add(5) # Não insere elementos repetidos
meu_set.add(6)
print(meu_set)

# update()
outro_set.update([4, 5, 6])
print(outro_set)

# discard()
meu_set.discard(4)
meu_set.discard(1)
print(meu_set)

# União
print(meu_set | outro_set)
print(meu_set.union(outro_set))

# Interseção
print(outro_set & meu_set)
print(outro_set.intersection(meu_set))

# Diferença
print(outro_set - meu_set)
print(meu_set.difference(outro_set))

# Diferença simétrica
print(meu_set ^ outro_set)
print(outro_set.symmetric_difference(meu_set))
