print('==' * 20)
print('Progressão Geométrica')
print('==' * 20)
print('<<< Para as variáveis da PG a seguir informe um número inteiro >>>')
A = int(input('Primeiro termo: '))
Limite = int(input('Quantidade de termos: '))
R = int(input('Razão: '))
print('Os valores da Progressão Geométrica são: ', end='PG = { ')
for i in range(1, Limite + 1):
    PG = A * (R ** (i - 1))  # Termo Geral de uma PG
    print(PG, end=' ')
print('}')
