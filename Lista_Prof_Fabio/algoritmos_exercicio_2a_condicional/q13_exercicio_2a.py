def main():
    print('Informe 5 números inteiros')
    n1 = int(input('1º num.: '))
    n2 = int(input('2º num.: '))
    n3 = int(input('3º num.: '))
    n4 = int(input('4º num.: '))
    n5 = int(input('5º num.: '))

    analisar_numeros(n1, n2, n3, n4)
    bigger = maior(n5, analisar_numeros(n1, n2, n3, n4))
    menor(n1, n2, n3, n4, n5)
    print('O maior número é:', bigger)

def analisar_numeros(x, y, z, w):
    if x == y == z == w:
        return x
    elif x >= y and z >= w or z <= w:
        if x >= z and x >= w:
            return x
        elif x <= z or x <= w:
            if z >= w:
                return z
            elif z <= w:
                return w

    elif x <= y and z >= w or z <= w:
        if y >= z and y >= w:
            return y
        elif y <= z or y <= w:
            if z >= w:
                return z
            elif z <= w:
                return w

def maior(a, b):
    if a >= b:
        return a
    elif a < b:
        return b

def menor(a, b, c, d, e):
   menor = a
   if b < a:
       menor = b
   if c < menor:
       menor = c
   if d < menor:
       menor = d
   if e < menor:
       menor = e
   print('o menor numero é: {}'.format(menor))

main()