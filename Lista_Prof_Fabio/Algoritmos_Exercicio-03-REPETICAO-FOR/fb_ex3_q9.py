def main():
    limite_inferior = int(input('Informe um valor para ser o limite inferior: '))
    limite_superior = int(input('Informe um valor para ser o limite superior: '))

    numeros_pares(limite_inferior, limite_superior)

def numeros_pares(inferior, supeior):
    print(f'Os números PARES no intervalo de {inferior} a {supeior} são: ', end=' ')
    for i in range(inferior, supeior + 1):
        if i % 2 == 0:
            print(i, end=' ')
main()