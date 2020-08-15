# ENTRADA
tempo_fumo = int(input('Quantos anos você é fumante? >> '))
cigarros_por_dia = int(input('Quantos cigarros fuma por dia? >> '))
preco_carteira = float(input('Qual o preço da carteira de cigarro? >> R$ '))

# PROCESSAMENTO
quantidade_cigarros = tempo_fumo * 365 * cigarros_por_dia
gasto_total_cigarros = (preco_carteira / 20) * quantidade_cigarros

# SAÍDA
print('==='*23)
print('Você fumante por {} anos já gastou R$ {:.2f} reais com cigarros.' .format(tempo_fumo, gasto_total_cigarros))
print('==='*23)