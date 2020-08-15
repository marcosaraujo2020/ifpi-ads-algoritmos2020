# Entrada
valor_dias = int(input('Informe uma quantidade de dias com valor inteiro: '))

# Processamento
quantidade_semana = valor_dias // 7
quantidade_dias = valor_dias % 7

# Saída
print('{} dia(s) corresponde a {} semana(s) e {} dia(s).'.format(valor_dias, quantidade_semana, quantidade_dias))

