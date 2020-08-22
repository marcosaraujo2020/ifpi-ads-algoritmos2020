def main():
    n = int(input('Informe número inteiro: '))
    numero = 1
    somatorio = 0
    while numero <= n:
        if numero % 2 == 1:
            somatorio += 1/numero
        else:
            somatorio -= 1/numero

        numero += 1
    print(f'A soma dos números é {somatorio}')

main()
