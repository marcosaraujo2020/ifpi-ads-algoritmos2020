print('==' * 20)
print('\033[1;33mProgressão Geométrica\033[m')
print('==' * 20)
print('<<< Para as variáveis da PG a seguir informe um número inteiro >>>')
A = int(input('Primeiro termo: '))
Limite = int(input('Quantidade de termos: '))
R = int(input('Razão: '))
print('Os valores da Progressão Geométrica são: ', end='PG = { ')
i = 1
while i <= Limite:
    PG = A * (R ** (i - 1))  # Termo Geral de uma PG
    print(PG, end=' ')
    i += 1
print('}')
