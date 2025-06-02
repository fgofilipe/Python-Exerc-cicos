import math
angulo = float(input('Digite a sua area em graus: '))
s = math.sin(math.radians(angulo))
b = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
print('O valor de SEN é {:.2f}'.format(s))
print('O valor de COS é {:.2f}'.format(b))
print('O valor de TAN é {:.2f}'.format(t))
