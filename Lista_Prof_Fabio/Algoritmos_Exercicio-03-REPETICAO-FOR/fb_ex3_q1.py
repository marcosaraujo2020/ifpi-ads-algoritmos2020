numeros = int(input('Informe um número inteiro: '))
print(f'Os números inteiros do intervalo de 1 a {numeros} são:', end=' ')
for n in range(1, numeros + 1):
    print(n, end=' ')
