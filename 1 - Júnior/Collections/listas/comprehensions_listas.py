lista_simples_inteiros = [1, 2, 3, 4, 5]
nova_lista = []

for i in lista_simples_inteiros:
    nova_lista.append(i*i)

print(lista_simples_inteiros)
print(nova_lista)

nova_lista_elegante = [i*i for i in lista_simples_inteiros]
print(nova_lista_elegante)

outra_lista_elegante = [i*i for i in range(1, 11)]
print(outra_lista_elegante)
