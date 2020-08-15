# ENTRADA
print('A seguir, informe dois pontos quaisquer para um plano')
x1 = int(input('Digite o valor para x1: '))
y1 = int(input('Digite o valor para y1: '))
x2 = int(input('Digite o valor para x2: '))
y2 = int(input('Digite o valor para y2: '))

# PROCESSAMENTO
distancia_pontos = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# SAÍDA
print('')
print('A distância entres os pontos ({}, {}) e ({}, {}) é de: {:.2f}' .format(x1, y1, x2, y2, distancia_pontos))