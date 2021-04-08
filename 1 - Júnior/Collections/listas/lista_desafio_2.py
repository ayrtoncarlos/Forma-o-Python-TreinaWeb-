lista = [int(i) for i in input().split()]

Q = int(input())

for _ in range(Q):
    query = input()
    
    if query.lower() == 'inserir':
        x, y = (int(i) for i in input().split())
        lista.insert(x, y)
    elif query.lower() == 'deletar':
        x = int(input())
        del lista[x]

print(' '.join([str(i) for i in lista]))
