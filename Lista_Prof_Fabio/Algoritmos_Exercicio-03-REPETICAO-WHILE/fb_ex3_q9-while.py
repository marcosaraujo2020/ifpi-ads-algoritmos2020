def main():
    limite_inferior = int(input('Informe um valor para ser o limite inferior: '))
    limite_superior = int(input('Informe um valor para ser o limite superior: '))

    numeros_pares(limite_inferior, limite_superior)

def numeros_pares(inferior, supeior):
    print(f'Os números PARES no intervalo de {inferior} a {supeior} são: ', end=' ')
    while inferior <= supeior:
        if inferior % 2 == 0:
            print(inferior, end=' ')
        inferior += 1
main()
