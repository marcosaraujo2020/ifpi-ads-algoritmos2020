print('='*20)
print('   Calcula Idade')
print('='*20)

# ENTRADA
print('Informe a seguir a data de hoje: ')
dia_atual = int(input('Qual o dia atual? '))
mes_atual = int(input('Qual o mês atual? '))
ano_atual = int(input('Qual o ano atual? '))

print('Agora, digite abaixo a data do seu aniversário: ')
dia_nascimento = int(input('Informe o dia: '))
mes_nascimento = int(input('Digite o mês em numeral: '))
ano_nascimento = int(input('Informe o ano do seu aniversário: '))

# PROCESSAMENTO
dia = dia_atual - dia_nascimento
mes = mes_atual - mes_nascimento
ano = ano_atual - ano_nascimento

# SAÍDA
if dia >= 0 and mes == 0 or dia <= 0 and mes > 0 or dia > 0 and mes > 0:
    print('Você tem {} anos de idade.'.format(ano))
else:
    print('Você tem {} anos de idade.'.format(ano - 1))

