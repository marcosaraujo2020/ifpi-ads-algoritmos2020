print('Informe dois números inteiros')
x = int(input('1º número: '))
y = int(input('2º número: '))

if x % y == 1:
    print(x + y + 1)
elif x % y == 2:
    if x % 2 == 0 and y % 2 == 0:
        print(f'{x} e {y} são par.')
    elif x % 2 == 0 and y % 2 != 0:
        print(f'{x} é par e {y} é ímpar.')
    elif x % 2 != 0 and y % 2 == 0:
        print(f'{x} é ímpar e {y} é par.')
    else:
        print(f'{x} e {y} são ímpares.')
elif x % y == 3:
    print((x + y) * x)
elif x % y == 4:
    print((x + y) / y)
else:
    print(x ** 2, 'e', y ** 2)
