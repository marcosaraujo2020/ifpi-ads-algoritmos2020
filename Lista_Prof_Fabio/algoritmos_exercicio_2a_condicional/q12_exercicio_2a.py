def main():
    num = int(input('Digite um número inteiro: '))

    par_ou_impar(num)

def par_ou_impar(n):
    if n % 2 == 0:
        print(f'{n} é par.')
    else:
        print(f'{n} é ímpar.')

main()