import carro, moto, veiculo, pessoa2

#help(carro.Carro)

uno_preto = carro.Carro("Preto", "Flex", 1.0, 4)
#help(uno_preto.abastecer)
uno_preto.ligar()
uno_preto.abastecer(30)
uno_preto.abastecer(25)
print(f"A quantidade de combustível do carro é: \n")
del uno_preto

uno_vermelho = carro.Carro("Vermelho", "Flex", 1.4, 2)
uno_vermelho.desligar()
print(f"A quantidade de combustível do uno_vermelho é: ")
uno_vermelho.acelerar()
print(f"A velocidade do uno_vermelho é: ")
uno_vermelho.ligar()
uno_vermelho.acelerar(80)
print(f"A velocidade do uno_vermelho é: \n")
uno_vermelho.pintar("preto")

moto_azul = moto.Moto("Azul", "Gasolina", 1.4, 1)
moto_azul.ligar()
moto_azul.abastecer(50)
moto_azul.acelerar(40)
print(f"A velocidade da moto_azul é: ")
moto_azul.abastecer(50)
moto_azul.pintar("Verde")
print(moto_azul.cor)
moto_azul.pintar("azul")

pessoa = pessoa2.Pessoa("Ayrton")

if isinstance(pessoa, veiculo.Veiculo):
    print("A classe é um veículo")
else:
    print("A classe não é um veículo")
