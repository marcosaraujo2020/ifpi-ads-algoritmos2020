# ENTRADA
tempo = int(input('Entre com um valor em minutos: '))

# PROCESSAMENTO
hora = tempo // 60
minutos = tempo % 60

# SAÍDA
print('---'*20)
print('O tempo de {} min., corresponde a {} hora(s) e {} minuto(s).' .format(tempo, hora, minutos))
print('---'*20)
