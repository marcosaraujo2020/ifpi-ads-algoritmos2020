# ENTRADA
print('A seguir, digite dois números:')
numero1 = float(input('Digite o 1º número: '))
numero2 = float(input('Digite o 2º número: '))

# PROCESSAMENTO
divisao = (numero1 + numero2) / (numero1 - numero2)

# SAÍDA
print('')
print('O resultado da divisão da soma pela diferença desses números é: {:.3f}'.format(divisao))
print('')