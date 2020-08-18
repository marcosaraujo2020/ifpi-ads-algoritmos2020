def main():
    limite_inferior = int(input('Informe um valor para ser o limite inferior: '))
    limite_superior = int(input('Informe um valor para ser o limite superior: '))

    numeros_primos(limite_inferior, limite_superior)

def numeros_primos(inferior, superior):
    print(f'Os números PRIMOS no intervalo de {inferior} a {superior} são: ', end=' ')
    cont = 1
    total = 0
    for c in range(inferior, superior + 1):
        if c % cont == 0:
            total += 1
            cont += 1
        if total == 2:
            print(c, end=' ')
main()

# for cont in range(inferior, supeior + 1):