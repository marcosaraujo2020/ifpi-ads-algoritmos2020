# Entrada
quatidade_segundos = int(input('Informe um numero inteiro em quantidade de segundos: '))

# Processamento
horas = quatidade_segundos // 3600
minutos = (quatidade_segundos % 3600) // 60
segundos = (quatidade_segundos % 3600) % 60

# Saída
print('{} segundo(s) corresponde a {} hora(s) {} minuto(s) e {} segundo(s).'.format(quatidade_segundos, horas, minutos, segundos))

