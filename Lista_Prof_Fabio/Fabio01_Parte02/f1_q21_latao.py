# ENTRADA
quantidade_latao = float(input('Informe a quantidade de latão em quilograma (Kg): '))

# PROCESSAMENTO
cobre = quantidade_latao * 0.70
zinco = quantidade_latao * 0.30

# SAÍDA
print('Para se obter {} Kg de latão, será necessário {:.1f} Kg de cobre e {:.1f} Kg de zinco.' .format(quantidade_latao, cobre, zinco))