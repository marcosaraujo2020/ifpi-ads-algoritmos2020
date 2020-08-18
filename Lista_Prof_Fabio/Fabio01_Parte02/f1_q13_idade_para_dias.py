# ENTRADA
print('A seguir, informe os dados que se pede da sua idade:')
ano = int(input('A sua idade em anos: '))
meses = int(input('Em meses: '))
dias = int(input('Em dias: '))

# PROCESSAMENTO
idade = ano * 365 + meses * 30 + dias

# SAÍDA
print("A sua idade em quantidade de dias é: {}" .format(idade))