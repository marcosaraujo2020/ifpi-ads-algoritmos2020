# ENTRADA
numero = int(input('Digite um número inteiro de 3 algarismos: '))

# PROCESSAMENTO
quociente1 = numero // 100
quociente2 = (numero % 100) // 10
quociente3 = ((numero % 100)) % 10

# SAÍDA
print('')
print('---'*20)
print('A soma das ordens dos elementos da C, D e U é igual a: {}'.format(quociente3 + quociente2 + quociente1))
print('---'*20)
print('')