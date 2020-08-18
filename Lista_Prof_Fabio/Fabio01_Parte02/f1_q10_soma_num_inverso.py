# Entrada
numero = int(input('Digite um número inteiro com 3 algarismos: '))

# Processamento
quociente1 = numero // 100
quociente2 = (numero % 100) // 10
quociente3 = ((numero % 100)) % 10
number1 = str(quociente1)
number2 = str(quociente2)
number3 = str(quociente3)
inverso = number3 + number2 + number1
number_inverso = int(inverso)
diferenca = numero + number_inverso

# Saída
print('O resultado da soma entre o número {} e seu inverso {} é de {}.'.format(numero, number_inverso, diferenca))