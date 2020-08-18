from time import sleep
print('---'*13)
print('        CAIXA ELETRÔNICO     ')
print('---'*13)
# ENTRADA
valor_saque = float(input('Informe qual o valor do saque: R$ '))

# PROCESSAMENTO
nota50 = int(valor_saque // 50)
nota10 = int((valor_saque % 50) // 10)
nota5 = int(((valor_saque % 50) % 10) // 5)
nota1 = int(((valor_saque % 50) % 10) % 5)

# SAÍDA
print('Contabilizando as notas ...')
sleep(3)
print('---'*13)
print('Notas disponíveis para o saque:')
print('---'*13)
print(nota50,'x R$ 50,00')
print(nota10,'x R$ 10,00')
print(nota5,'x R$ 5,00')
print(nota1,'x R$ 1,00')
print('---'*13)
print('Confirme para concluir seu saque.')
print('---'*13)

