def main():
    print('A seguir digite dois números:')
    n1 = int(input('1º Número: '))
    n2 = int(input('2º Número: '))

    maior_ou_menor(n1, n2)

def maior_ou_menor(x, y):
    if x > y:
        print(f'{x} é maior que {y}.')
    elif x < y:
        print(f'{x} é menor que {y}.')
    else:
        print('Os dois são iguais.')

main()
