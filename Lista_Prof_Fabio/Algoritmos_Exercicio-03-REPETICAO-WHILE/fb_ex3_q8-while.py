def main():
    N = int(input('Digite um número inteiro: '))
    limite_inferior = int(input('Informe um valor para o limite inferior: '))
    limite_superior = int(input('Informe um valor para o limite superior: '))

    multiplo(N, limite_inferior, limite_superior)

def multiplo(numero, inferior, supeior):
    print(f'Os números no intervalo de {inferior} a {supeior} que são múltiplos de {numero} são: ',end=' ')
    while inferior <= supeior:
        if inferior % numero == 0:
            print(inferior, end=' ')
        inferior += 1
main()