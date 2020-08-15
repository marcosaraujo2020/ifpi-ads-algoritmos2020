# Entrada
quantidade_meses = int(input('Informe um numero inteiro para a quantidade(s) de mes(es): >> '))

# Processamento
anos = quantidade_meses // 12
meses = quantidade_meses % 12

# Saída
print('{} mes(es) representa {} ano(s) e {} mes(es).'.format(quantidade_meses, anos, meses))

