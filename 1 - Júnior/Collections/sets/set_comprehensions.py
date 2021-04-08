# Criando um set comprehensions

set_comprehensions = {i*i for i in range(10)}

print(type(set_comprehensions))
print(set_comprehensions)

set_1 = {1, 2, 3}
set_2 = {4, 5, 6}

outro_set_comprehensions = {i for i in set_1.union(set_2)}

print(type(outro_set_comprehensions))
print(outro_set_comprehensions)
