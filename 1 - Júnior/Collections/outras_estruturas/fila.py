from collections import deque

minha_fila = deque(['Ayrton', 'Mateus', 'Felipe'])
print(minha_fila)

# Adicionando elemento em uma fila
minha_fila.append('Cristine')
print(minha_fila)

# Removendo elemento de uma fila
minha_fila.popleft()
print(minha_fila)
