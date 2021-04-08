# 0 | 1 | 2 | 3 | 4 --> Índices
# 5 | 3 | 1 | 4 | 2 --> Valores

numeros = list()
tamanho = int(input('Digite o tamanho do vetor: '))
for i in range(tamanho):
    valor = int(input(f'Digite o número para a posição do vetor {i}: '))
    numeros.append(valor)

print("Vetor: ", numeros)
print('Posição 1: ', numeros[1])

# BUSCA LINEAR
numero_pesquisar = int(input('Digite o valor a ser pesquisado no vetor: '))
posicao_resultado = -1
for i in range(tamanho):
    if numeros[i] == numero_pesquisar:
        posicao_resultado = i
        break
if posicao_resultado < 0:
    print('O elemento não foi encontrado no vetor')
else:
    print(f'O elemento foi encontrado na posição {posicao_resultado}')
# FIM DA BUSCA LINEAR

# SELECTION_SORT
for i in range(tamanho):
    indice_menor = i
    for j in range(i+1, tamanho):
        if numeros[j] < numeros[indice_menor]:
            indice_menor = j
    temp = numeros[indice_menor]
    numeros[indice_menor] = numeros[i]
    numeros[i] = temp
    print('Vetor: ', numeros)
# FIM DO SELECTION SORT

# BUSCA BINÁRIA
resultado = -1
inicio = 0
meio = 0
fim = tamanho - 1
alvo = int(input('Digite o valor a ser procurado no vetor: '))
while inicio <= fim:
    meio = inicio + (fim - inicio) // 2
    if numeros[meio] < alvo:
        inicio = meio + 1
    elif numeros[meio] > alvo:
        fim = meio - 1
    else:
        resultado = meio
        break
if resultado < 0:
    print('Elemento não encontrado')
else:
    print(f'O elemento {alvo} está na posição {resultado}')
# FIM DA BUSCA BINÁRIA
