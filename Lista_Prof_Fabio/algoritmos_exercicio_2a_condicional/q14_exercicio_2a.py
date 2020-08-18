def main():
    n1 = int(input('1° numero: '))
    n2 = int(input('2° numero: '))
    n3 = int(input('3° numero: '))
    n4 = int(input('4° numero: '))
    n5 = int(input('5° numero: '))

    maior_que_media(n1, n2, n3, n4, n5)

def maior_que_media(a, b, c, d, e):
    med = (a + b + c + d + e) / 5
    print('A média dos valores é: ', med)

    print('Valor(es) acima da média:')
    if a > med:
        print(a)
    if b > med:
        print(b)
    if c > med:
        print(c)
    if d > med:
        print(d)
    if e > med:
        print(e)

main()