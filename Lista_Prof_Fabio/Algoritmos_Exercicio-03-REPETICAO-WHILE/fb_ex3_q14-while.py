def main():
    numero = int(input('Digite um número inteiro: '))
    maior_quadrado(numero)

def maior_quadrado(number):
    print(f'O maior quadrado menor ou igual que {number} é', end=' ')
    maior = 0
    valor = 1
    while valor <= number:
        quadrado = valor ** 2
        valor += 1
        if quadrado > maior and quadrado <= number:
            maior = quadrado
    print(f'>> \033[1;32m{maior}')
    print('')
main()
