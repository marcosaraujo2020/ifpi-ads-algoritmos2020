numero = int(input('Digite um número inteiro: '))
valor = 0
print(f'A sequência dos números são >>>', end=' ')
i = 1
while i <= numero: 
    print(f'\033[1;33m{i + valor}\033[m', end=' ')
    valor += i
    i += 1
print('<<< Fim..')
