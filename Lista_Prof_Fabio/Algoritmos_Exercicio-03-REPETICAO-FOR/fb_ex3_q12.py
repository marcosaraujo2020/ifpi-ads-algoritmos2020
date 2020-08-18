numero = int(input('Digite um número inteiro: '))
total = soma = 0
for c in range(1, numero + 1):
    lista_numeros = float(input('Informe um número: '))
    total += 1
    soma += lista_numeros
media = soma / total
print(f'A \033[1;31msoma\033[m dos números é igual a \033[1;31m{soma}\033[m e a \033[1;33mmédia\033[m de todos os números foi \033[1;33m{media}')
