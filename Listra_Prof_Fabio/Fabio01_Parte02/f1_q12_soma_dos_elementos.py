# ENTRADA
numero = int(input('Digite um número inteiro com 4 algarismos: '))

# PROCESSAMENTO
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = ((numero % 100) % 100) // 10
unidade = ((numero % 100) % 100) % 10
soma = milhar + centena + dezena + unidade

# SAÍDA
print('A soma dos elementos que compõe o número {} é: {}'.format(numero, soma))
