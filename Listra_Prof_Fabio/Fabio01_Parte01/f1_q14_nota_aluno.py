# ENTRADA
nota1 = float(input('Digite o valor da 1ª nota: '))
peso1 = float(input('Informe o peso da 1ª nota: '))
nota2 = float(input('Digite o valor da 2ª nota: '))
peso2 = float(input('Informe o peso da 2ª nota: '))
nota3 = float(input('Digite o valor da 3ª nota: '))
peso3 = float(input('Informe o peso da 3ª nota: '))

# PROCESSAMENTO
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# SAÍDA
print('')
print('---'*20)
print('A média ponderada da nota do aluno é: {:.1f}'.format(media))
print('---'*20)