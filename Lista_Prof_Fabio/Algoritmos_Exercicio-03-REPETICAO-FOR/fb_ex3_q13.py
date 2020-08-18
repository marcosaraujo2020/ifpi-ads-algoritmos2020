numero = int(input('Digite um número inteiro: '))
maior = 0
for c in range(1, numero + 1):
    lista_numeros = int(input('Informe um número: '))
    if lista_numeros > maior:
        maior = lista_numeros
print(f'O \033[1;31mMAIOR\033[m número da lista é \033[1;31m{maior}\033[m')
