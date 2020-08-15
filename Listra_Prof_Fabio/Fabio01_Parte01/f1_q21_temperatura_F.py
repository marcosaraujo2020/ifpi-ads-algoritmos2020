# ETRADA
temp_fahrenheit = float(input('Inforne um valor da temperatura em Fahrenheit (F): '))

# PROCESSAMENTO
temp_celsius = (5 * temp_fahrenheit - 160) / 9

# SAÍDA
print('')
print('A temperatura de {:.2f} Fahrenheit representa {:.2f} graus Celsius.'.format(temp_fahrenheit, temp_celsius))
print('')