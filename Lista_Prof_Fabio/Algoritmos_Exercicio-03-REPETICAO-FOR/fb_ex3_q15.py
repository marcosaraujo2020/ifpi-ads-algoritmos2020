numero = int(input('Digite um número inteiro: '))
valor = 0
for i in range(1, numero + 1):
    print(i + valor, end=' ')
    valor += i
