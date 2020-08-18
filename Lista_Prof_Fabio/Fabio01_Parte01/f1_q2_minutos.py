# ENTRADA
horas = int(input('Digite um valor em horas: '))
minutos = int(input('Digite um valor em minutos: '))

# PROCESSAMENTO
tempo_total = horas * 60 + minutos

# SAÍDA
print('')
print('='*40)
print('O tempo total em minutos é de: {} min.'.format(tempo_total))
print('='*40)