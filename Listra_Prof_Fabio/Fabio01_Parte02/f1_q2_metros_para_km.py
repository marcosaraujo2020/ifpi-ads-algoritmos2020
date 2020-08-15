# Entrada
medida = int(input('Digite um valor inteiro para a medida em metros: '))

# Processamento
medida_quilometros = medida // 1000
medida_metros = medida % 1000

# Saída
print('A medida de {} m corresponde a {} Km e {} m. '.format(medida, medida_quilometros, medida_metros))
