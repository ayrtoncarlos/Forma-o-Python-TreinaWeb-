from os import path

dir = path.dirname(path.realpath(__file__))

arquivo = open(dir + '/texto.txt', 'a')
arquivo.close()

if path.exists("texto.txt"):
    print("O arquivo texto.txt existe.")
else:
    print("O arquivo texto.txt não existe.")