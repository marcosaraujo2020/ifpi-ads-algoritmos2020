def main():
    n = int(input('Digite um número: '))
    numero = 1
    soma = 0
    while n >= 1:
        if numero % 2 != 0:
            soma += numero / n
        else:
            soma -= n / numero
        
        n -= 1
        numero += 1
    
    print(f'A soma é {soma}')

main()
