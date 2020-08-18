# Entrada
quantidade_minutos = int(input('Informe um numero inteiro para a quantidade de minutos: >> '))

# Processamento
dias = quantidade_minutos // 1440
horas = (quantidade_minutos % 1440) // 60
minutos = (quantidade_minutos % 1440) % 60

# Saída
print('{} minuto(s) representam {} dia(s) {} hora(s) e {} minuto(s).'.format(quantidade_minutos, dias, horas, minutos))