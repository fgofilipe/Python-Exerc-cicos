d = float(input('Quantod dias você ficou com o carro? '))
km = float(input('Quantos Km você rodou? '))
dias = d * 60
kilometros = km * 0.15
carro = dias + kilometros
print('O valor total pagar é de {}R$'.format(carro))