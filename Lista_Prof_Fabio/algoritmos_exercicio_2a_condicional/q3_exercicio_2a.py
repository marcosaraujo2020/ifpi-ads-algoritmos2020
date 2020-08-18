def main():
    print('A seguir digite três números inteiros:')
    n1 = int(input('1º Número: '))
    n2 = int(input('2º Número: '))
    n3 = int(input('3º Número: '))

    numero_maior(n1, n2, n3)

def numero_maior(x, y, z):
    if y < x > z or x == y > z or x == z > y:
        print(f'{x} é o maior número.')
    elif x < y > z or y == z > x:
        print(f'{y} é o maior número.')
    elif x < z > y:
        print(f'{z} é o maior número.')
    else:
        print('Todos os números são iguais.')

main()