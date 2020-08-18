print('-='*20)
print('\033[31mFatorial de um Número\033[m')
print('-='*20)
num = int(input('Informe um número inteiro: '))
print(f'O fatorial de {num}! =', end=' ')
fatorial = 1
while num > 1:
    print(num, end=' x ')
    fatorial = fatorial * num
    num -= 1
print('1 =', fatorial)
