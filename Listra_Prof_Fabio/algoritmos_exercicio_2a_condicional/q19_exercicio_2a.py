print('-'*20)
print('Cálculo IMC')
print('-'*20)

altura = float(input('Qual a medida da sua altura em metros?: '))
peso = float(input('Informe qual o seu peso em Kg: '))
imc = peso / (altura ** 2)
print('Seu IMC é: {:.2f}'.format(imc))

if imc < 25.0:
    print('Peso Normal')
elif imc <= 30:
    print('Obeso')
elif imc > 30:
    print('Obesidade Mórbida')
