from os import path
import fileinput

mensagem = input()

dir = path.dirname(path.realpath(__file__))

try:
    with open(dir + '/texto.txt', 'a') as f:
        f.write(f'{mensagem}\n')
except FileNotFoundError:
    print('Arquivo não encontrado')

with fileinput.input(files=('texto.txt')) as f:
    for line in f:
        print(line)
