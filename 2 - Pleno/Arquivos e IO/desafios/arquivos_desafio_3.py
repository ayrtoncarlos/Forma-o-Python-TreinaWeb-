from io import FileIO
from os import path
import fileinput

t = int(input())

dir = path.dirname(path.realpath(__file__))

try:
    with FileIO(dir + "/texto.txt", "a") as file:
        for i in range(0, t):
            mensagem = input() + '\n'
            file.write(mensagem.encode())
except FileNotFoundError:
    print('Arquivo não encontrado')

try:
    with fileinput.input(files=('texto.txt')) as f:
        for line in f:
            print(line[:-1])
except FileNotFoundError:
    print('Arquivo não encontrado')
