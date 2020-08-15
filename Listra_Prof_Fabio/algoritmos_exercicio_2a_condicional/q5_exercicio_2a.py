def main():
    print('Informe três numeros a seguir: ')
    n1 = int(input('1º Número: '))
    n2 = int(input('2º Número: '))
    n3 = int(input('3º Número: '))

    ordem_crescente(n1, n2, n3)

def ordem_crescente(x, y, z):
    if x < y < z or x < y == z or x == y < z:
        print(f'Ordem crescente dos números: {x}, {y} e {z}.')
    elif x < z < y or x == z < y:
        print(f'Ordem crescente dos números: {x}, {z} e {y}.')
    elif y < x < z or y < x == z:
        print(f'Ordem crescente dos números: {y}, {x} e {z}.')
    elif y < z < x or y == z < x:
        print(f'Ordem crescente dos números: {y}, {z} e {x}.')
    elif z < x < y or z < x == y or z == x < y:
        print(f'Ordem crescente dos números: {z}, {x} e {y}.')
    elif z < y < x:
        print(f'Ordem crescente dos números: {z}, {y} e {x}.')
    elif x == y == z:
        print('Todos números são iguais.')

main()