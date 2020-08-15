from time import sleep
print('---'*13)
print('         LOJA DA ALEGRIA     ')
print('---'*13)
# ENTRADA
valor_mercadoria = float(input('Informe o valor da compra: R$ '))

# PROCESSAMENTO
valor_entrada = (valor_mercadoria // 3) + (valor_mercadoria % 3)
valor_parcelas = valor_mercadoria // 3

# SAÍDA
print('')
print("Processando as informações.....")
sleep(3)
print('')

print('---'*13)
print('        RESUMO DA COMPRA     ')
print('---'*13)
print('Valor total da compra: R$ {:.2f}'.format(valor_mercadoria))
print('Entrada: R$ {:.2f}'.format(valor_entrada))
print('Parcelas: 2 x de R$ {:.2f}'.format(valor_parcelas))
print('---'*13)
print('Obrigado pela escolha, volte sempre!!!!')
print('---'*13)
