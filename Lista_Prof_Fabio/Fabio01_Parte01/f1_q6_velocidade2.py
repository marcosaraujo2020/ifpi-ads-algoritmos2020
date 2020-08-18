print('---'*15)
print('Converter Velocidade Km/h para m/s')
print('---'*15)

# ENTRADA
velocidade_kmh = float(input('Digite o valor da velocidade em Km/h: '))

# PROCESSAMENTO
velocidade_ms = velocidade_kmh / 3.6

# SAÍDA
print('=='*25)
print('A velocidade de {:.2f} Km/h corresponde a {:.2f} m/s.' .format(velocidade_kmh, velocidade_ms))
print('=='*25)