larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
area = larg * alt
print('A sua parede tem a dimensão de {}x{} e sua área é de {}m2.'.format(larg, alt, area))
tinta = area / 2
print('E voce irá precisar de {} litros de tinta.'.format(tinta))
