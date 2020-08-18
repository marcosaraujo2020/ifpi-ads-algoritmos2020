# ENTRADA
numero = int(input('Digite um número inteiro de 3 algarismos: '))

# PROCESSAMENTO
quociente1 = numero // 100
quociente2 = (numero % 100) // 10
quociente3 = ((numero % 100)) % 10

# SAÍDA
print('')
print('---'*13)
print('Número escolhido: {}'.format(numero))
print('O inverso do número escolhido: {}{}{}'.format(quociente3, quociente2, quociente1))
print('---'*13)
print('')

