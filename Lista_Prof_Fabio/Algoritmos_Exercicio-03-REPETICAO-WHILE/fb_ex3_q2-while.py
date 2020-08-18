numeros = int(input('Informe um número inteiro: '))
print(f'Os números inteiros pares no intervalo de 1 a {numeros} são:', end=' ')
n = 1
while n <= numeros: 
    if n % 2 == 0:
        print(n, end=' ')
    n += 1
print('Fim...')
