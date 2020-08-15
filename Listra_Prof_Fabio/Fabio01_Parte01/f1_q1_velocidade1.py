print('--'*20)
print('Converter Velocidade m/s para Km/h')
print('--'*20)

# ENTRADA
velocidade_ms = float(input('Digite o valor da velocidade em m/s: '))

# PROCESSAMENTO
velocidade_kmh = velocidade_ms * 3.6

# SAÍDA
print('A velocidade de {:.2f} m/s corresponde a {:.2f} km/h.' .format(velocidade_ms, velocidade_kmh))
print('')


