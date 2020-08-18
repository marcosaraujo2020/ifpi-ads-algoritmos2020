# ENTRADA
binario = int(input('Digite um número inteiro binário com 4 digitos: '))

# PROCESSAMENTO
digito0 = binario % 10
digito1 = (binario // 10) % 10
digito2 = ((binario // 10) // 10) % 10
digito3 = ((binario // 10) // 10) // 10

decimal = (digito3 * 2 ** 3) + (digito2 * 2 ** 2) + (digito1 * 2 ** 1) + (digito0 * 2 ** 0)

# SAÍDA
print('Número binário: {}{}{}{}'.format(digito3, digito2, digito1, digito0))
print('Número decimal correspondente é: {}'.format(decimal))





# PROCESSAMENTO
# digito0 = binario % 2
# digito1 = (binario // 2) % 2
# digito2 = (binario // 4) % 2
# digito3 = (binario // 6) % 2
# decimal = (digito3 * 2 ** 3) + (digito2 * 2 ** 2) + (digito1 * 2 ** 1) + (digito0 * 2 ** 0)