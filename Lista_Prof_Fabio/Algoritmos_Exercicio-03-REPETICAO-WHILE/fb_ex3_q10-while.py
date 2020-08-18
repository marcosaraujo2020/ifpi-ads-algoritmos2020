def main():
    limite_inferior = int(input('Informe um valor para ser o limite inferior: '))
    limite_superior = int(input('Informe um valor para ser o limite superior: '))

    numeros_impares(limite_inferior, limite_superior)

def numeros_impares(inferior, supeior):
    print(f'Os números ÍMPARES no intervalo de {inferior} a {supeior} são: ', end=' ')
    while inferior <= supeior:
        if inferior % 2 == 1:
            print(inferior, end=' ')
        inferior += 1
main()
