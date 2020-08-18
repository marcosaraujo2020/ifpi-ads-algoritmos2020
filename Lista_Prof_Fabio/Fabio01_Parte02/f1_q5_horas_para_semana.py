# Entrada
valor_horas = int(input('Informe a quantidade de horas em número inteiro: '))

# Processamento
semana = valor_horas // 168
dias = (valor_horas % 168) // 24
horas = (valor_horas % 168) % 24

# Saída
print('{} horas(s) corresponde a {} semana(s) {} dia(s) e {} horas(s).'.format(valor_horas, semana, dias, horas))