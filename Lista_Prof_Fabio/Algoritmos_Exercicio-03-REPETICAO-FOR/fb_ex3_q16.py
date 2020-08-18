print('-==' * 10)
print('\033[1;32mSequência de Fibonacci\033[m')
print('-==' * 10)
numero = int(input('Digite um número inteiro: '))
n1 = 0
n2 = 1
print(f'A \033[1;31msequência fibonacci\033[m é \033[1;36m{n1}\033[m - \033[1;36m{n2}\033[m', end=' - ')
for c in range(2, numero):
    n3 = n1 + n2
    c = n3
    print(f'\033[1;36m{c}\033[m', end=' - ')
    n1 = n2
    n2 = n3
print('Fim')
print('')