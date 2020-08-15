# ENTRADA
print('A seguir digite três numeros qualquer:')
numero1 = float(input('Digite o 1º número: '))
numero2 = float(input('Digite o 2º número: '))
numero3 = float(input('Digite o 3º número: '))

# PROCESSAMENTO
media = (numero1 + numero2 + numero3) / 3

# SAÍDA
print('A média dos 3 numeros escolhidos é: {:.2f}' .format(media))