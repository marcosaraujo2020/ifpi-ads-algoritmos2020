def main():
    n = int(input('Informe número inteiro: '))
    numero = 1
    soma = 0
    while numero <= n:
        expressao = 1/numero
        soma = soma + expressao
        numero += 1
    print(f'A soma dos números é {soma}')

main()
