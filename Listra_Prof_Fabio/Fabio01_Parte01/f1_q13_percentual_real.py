# ENTRADA
valor_real = float(input('Entre com qualquer valor em real: R$ '))

# PROCESSAMENTO
novo_valor_real = valor_real * 0.70

# SAÍDA
print('***'*20)
print('70% do valor R$ {:.2f} corresponde a R$ {:.2f} reais.'.format(valor_real, novo_valor_real))
print('***'*20)