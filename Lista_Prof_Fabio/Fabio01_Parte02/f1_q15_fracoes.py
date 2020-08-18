from fractions import Fraction
# ENTRADA
print(('--'*10))
print('Soma de Frações')
print('--'*10)
numerador1 = int(input('Informe o valor do 1º numerador: '))
denominador1 = int(input('Digite o valor do 1º denominador: '))
numerador2 = int(input('Forneça o valor para o 2º numerador: '))
denominador2 = int(input('Digite o valor para o 2º denominador: '))

# PROCESSAMENTO
mmc = denominador1 * denominador2
numerador_final = int((mmc / denominador1) * numerador1 + (mmc / denominador2) * numerador2)

# SAÍDA
print('---'*15)
print('A soma das frações {}/{} e {}/{} é de: {}/{}'.format(numerador1, denominador1, numerador2, denominador2, numerador_final, mmc ))
print('---'*15)