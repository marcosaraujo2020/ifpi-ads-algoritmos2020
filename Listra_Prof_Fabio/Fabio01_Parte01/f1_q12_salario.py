# ENTRADA
salario = float(input('Entre com o valor do salário do funcionário: R$ '))

# PROCESSAMENTO
novo_salario = salario + salario * 0.25

# SAÍDA
print('----'*20)
print('O salário do trabalhador de R$ {:.2f} houve um reajuste de 25% e terá como novo salário o valor de R$ {:.2f} reais.'.format(salario, novo_salario))
print('----'*20)