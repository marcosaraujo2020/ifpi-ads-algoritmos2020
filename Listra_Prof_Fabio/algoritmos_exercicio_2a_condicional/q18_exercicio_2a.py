print('Informe dois valores a seguir:')
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
print('-'*20)
print('Operações Básica')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('-'*20)

x = int(input('Escolha um dos itens acima para a operação: '))

if x == 1:
    print(f'A soma de {n1} + {n2} = {n1 + n2}')
elif x == 2:
    print(f'A Subtração de {n1} - {n2} = {n1 - n2}')
elif x == 3:
    print(f'A Multiplicação de {n1} x {n2} = {n1 * n2}')
elif x == 4:
    print(f'A Divisão de {n1} / {n2} =  {n1 / n2}')
else:
    print('Item inválido!')



