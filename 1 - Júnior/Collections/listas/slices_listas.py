lista_simples_inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_simples_inteiros)

print(lista_simples_inteiros[0:4])
print(lista_simples_inteiros[1:])
print(lista_simples_inteiros[:3])

nova_lista = lista_simples_inteiros[:3]
print(nova_lista)

intervalo = slice(1, 4)
print(lista_simples_inteiros[intervalo])
