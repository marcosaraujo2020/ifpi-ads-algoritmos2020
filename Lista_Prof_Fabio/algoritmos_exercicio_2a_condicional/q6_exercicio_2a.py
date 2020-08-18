def main():
    print('Informe três valores em angulos para formar um triângulo: ')
    angle1 = float(input('1º valor: '))
    angle2 = float(input('2º valor: '))
    angle3 = float(input('3º valor: '))

    formar_triangulo(angle1, angle2, angle3)

def formar_triangulo(alf, bet, gam):
    if alf + bet + gam > 180 or alf + bet + gam < 180 or alf == 0 or bet == 0 or gam == 0:
        print('Não forma um triângulo.')
    elif alf + bet + gam == 180 and alf < 90 and bet < 90 and gam < 90:
        print('TRIÂNGULO ACUTÂNGULO')
    elif alf + bet + gam == 180 and alf == 90 or bet == 90 or gam == 90:
        print('TRIÂNGULO RETÂNGULO')
    elif alf + bet + gam == 180 and alf > 90 or bet > 90 or gam > 90:
        print('TRIÂNGULO OBTUSÂNGULO')

main()