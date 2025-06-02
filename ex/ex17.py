import math
ca = float(input('Qual o valor do cateto adjascente? '))
co = float(input('Qual o valor do cateto oposto? '))
hip = math.hypot (ca, co)
print('A hipotenusa dos valores é {:.2f}' .format(hip))
