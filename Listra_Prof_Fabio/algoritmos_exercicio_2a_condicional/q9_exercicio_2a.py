def main():
    n = int(input('Digite um número inteiro entre 0 e 100: '))
    number_primo(n)

def number_primo(x):
    if x > 11:
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
            print('Este número não é primo.')
        else:
            print('Número primo.')
    if x <= 11:
        if x == 9 or x == 1:
            print('Este número não é primo.')
        elif x % 2 == 1 or x == 2:
            print('Número primo.')
        else:
            print('Este número não é primo.')

main()

