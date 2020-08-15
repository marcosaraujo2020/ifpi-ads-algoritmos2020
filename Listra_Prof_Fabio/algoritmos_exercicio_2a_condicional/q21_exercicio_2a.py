numero = float(input('Digite um numero real: '))

parte_fracionaria = numero - int(numero)

if parte_fracionaria >= 0.5:
    print('O número arrendondado é:', round(numero))
else:
    print('O número arredondado é:', int(numero))