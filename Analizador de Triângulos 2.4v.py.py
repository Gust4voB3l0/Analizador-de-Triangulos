r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmanto: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima PODERM FORMAR UM triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3:
        print('ESCALENO!')
    else:
        print('ISOCELES!')
else:
    print('Os Segmentos acima NÂO PODEM FORMAR UM TRIÂNGULO!')