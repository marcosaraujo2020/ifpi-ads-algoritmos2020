print('==' * 20)
print('Progressão Aritmética')
print('==' * 20)
print('<<< Para as variáveis da PA a seguir informe um número inteiro >>>')
A = int(input('Primeiro termo: '))
Limite = int(input('Quantidade de termos: '))
R = int(input('Razão: '))
print('Os valores da Progressão Aritmética são: ', end='PA = { ')
i = 1
while i <= Limite:
    PA = A + (i - 1) * R  # Termo Geral de uma PA
    print(PA, end=' ')
    i += 1
print('}')



