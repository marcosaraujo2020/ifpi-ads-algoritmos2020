print('Círculo Trignométrico')
angulo = int(input('Digite o valor de um angulo: '))

if 0 <= angulo <= 90:
    print(f'{angulo} graus - 1º Quadrante')
elif 90 < angulo <= 180:
    print(f'{angulo} graus - 2º Quadrante')
elif 180 < angulo <= 270:
    print(f'{angulo} graus - 3º Quadrante')
elif 270 < angulo <= 360:
    print(f'{angulo} graus - 4º Quadrante')