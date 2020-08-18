def main():
    print('A seguir digite um número inteiro com dois algarismo:')
    numero = int(input('Informe o numeral: '))
    
    comparar_numero(numero)

def comparar_numero(x):
    quociente = x // 10
    resto = x % 10
    if quociente == resto:
        print('Os algarismos das Dezenas e Unidades são iguais.')
    else:
        print('Os algarismos das Dezenas e Unidades são diferentes.')

main()