import random
n1 = str(input('Digite o nome: '))
n2 = str(input('Digite o nome: '))
n3 = str(input('Digite o nome: '))
n4 = str(input('Digite o nome: '))
lista = [n1, n2, n3, n4]
ordem = random.shuffle(lista)
print('A ordem de apresentação será:{}'.format(lista))