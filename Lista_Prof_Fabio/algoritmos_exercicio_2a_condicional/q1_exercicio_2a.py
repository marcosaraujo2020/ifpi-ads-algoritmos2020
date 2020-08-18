def main():
    a = int(input('Digite 1º número inteiro: '))
    b = int(input('Digite 2º número inteiro: '))
    c = int(input('Digite 3º número inteiro: '))

    avaliar_numeros(a, b, c)
    

def avaliar_numeros(x, y, z):
    if x == y == z:
        print(f'Todos os números são iguais.')
    elif x == y != z or x == z != y or x != y == z:
        print(f'2 números são iguais.')
    else:
        print('Todos os números sao diferentes.')

main()