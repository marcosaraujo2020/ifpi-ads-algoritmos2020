def main():
    num = int(input('Digite um número: '))
    numero = 1
    soma = 0
    n = num
    while numero <= num:
        #expressao = numero / n
        soma += numero / n
        n = n - 1
        numero += 1
    print(f'O Resultado da soma é {soma}')

main()
