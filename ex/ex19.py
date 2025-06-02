import random
a1 = str(input('Digite a primeira palavra: '))
a2 = str(input('Digite a segunda palavra: '))
a3 = str(input('Digite a terceira palavra: '))
a4 = str(input('Digite a quarta palavra: '))
lista = [a1, a2, a3, a4]
e = random.choice(lista)
print('A palavra escolhido foi {}. '.format(e))
