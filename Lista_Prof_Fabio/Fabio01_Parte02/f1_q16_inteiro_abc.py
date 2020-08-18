# ENTRADA
print('Digite 3 números inteiros e positivos a seguir')
A = int(input('primeiro número: '))
B = int(input('segundo número: '))
C = int(input('terceiro número: '))

# PROCESSAMENTO
R = (A + B) ** 2
S = (B + C) ** 2
D = int((R + S) / 2)

# SAÍDA
print(('---'*20))
print('O resultado da expressão D = (R + S) / 2 é igual a: {}' .format(D))