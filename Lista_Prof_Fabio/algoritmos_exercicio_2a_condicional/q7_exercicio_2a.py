def main():
    print('Informe três valores para os lados do triângulo:')
    x = int(input('1º valor: '))
    y = int(input('2º valor: '))
    z = int(input('3º valor: '))

    triangulo(x, y, z)

def triangulo(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        print('Os valores não forma um triâgulo.')
    elif a == 0 or b == 0 or c == 0:
        print('Não existe lado de triângulo com tamanho zero.')
    elif a == b == c:
        print('Triângulo Equilátero.')
    elif a == b != c or a != b == c or a == c != b:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')

main()
