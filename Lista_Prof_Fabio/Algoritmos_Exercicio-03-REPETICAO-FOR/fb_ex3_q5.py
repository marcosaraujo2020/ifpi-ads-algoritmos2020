print('-='*20)
print('Fatorial de um Número')
print('-='*20)
num = int(input('Informe um número inteiro: '))
print(f'O fatorial de {num}! =', end=' ')
fatorial = 1
for c in range(num, 1, -1):
    print(num, end=' x ')
    fatorial = fatorial * num
    num = num - 1
print('1 =', fatorial)
