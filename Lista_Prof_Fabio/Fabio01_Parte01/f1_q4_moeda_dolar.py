# ENTRADA
cotacao_dolar = float(input('Digite o valor da cotação do dolar hoje? U$ '))
valor_dolar = float(input('Digite qualquer valor em dólar: U$ '))

# PROCESSAMENTO
valor_real =  valor_dolar * cotacao_dolar

# SAÍDA
print('--'*30)
print('O valor de U$ {:.2f} é equivalente a R$ {:.2f} reais.'.format(valor_dolar, valor_real))
print('--'*30)