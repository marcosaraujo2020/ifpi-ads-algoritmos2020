# ENTRADA
idade = int(input('Qual a sua idade em quantidade de dias: '))

# PROCESSAMENTO
anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30


# SAÍDA
print("Você tem {} anos {} meses e {} dias de idade." .format(anos, meses, dias))