print('--'*11)
print('Custo de Veículo Novo')
print('--'*11)

# ENTRADA
custo_fabrica = float(input('Informe o valor do veículo no custo de fábrica: R$ '))

# PROCESSAMENTO
custo_consumidor = custo_fabrica + custo_fabrica * 0.28 + custo_fabrica * 0.45

# SAÍDA
print('-----'*12)
print('O valor do veículo ao consumidor final será de R$ {:.2f} reais.' .format(custo_consumidor))
print('-----'*12)