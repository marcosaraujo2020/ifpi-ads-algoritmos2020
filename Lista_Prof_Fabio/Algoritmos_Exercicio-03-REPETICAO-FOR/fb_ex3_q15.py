numero = int(input('Digite um número inteiro: '))
valor = 0
print(f'A sequência dos números são >>>', end=' ')
for i in range(1, numero + 1):
    print(i + valor, end=' ')
    valor += i
