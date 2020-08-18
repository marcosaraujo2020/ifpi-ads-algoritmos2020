numeros = int(input('Informe um número inteiro: '))
print(f'Os números inteiros pares no intervalo de 1 a {numeros} são:', end=' ')
for n in range(1, numeros + 1):
    if n % 2 == 0:
        print(n, end=' ')
