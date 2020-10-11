def main():
    n = int(input('Informe qual a ordem da matriz quadrada: '))
    matriz = []
    i = 0
    while i < n:
        lista = []
        for c in range(n):
            lista.append(int(input(f'Para i = {i} e j = {c} digite um valor: ')))
        matriz.append(lista)
        i += 1

    print('=='*30)
    for c in matriz:
        print(c)

    print()
    verificar = diagonal_principal(matriz)
    analisar = diagonal_secundaria(matriz)
    calcular = soma_demais_valores(matriz)
    print(f'A soma dos valores da Diagonal Principal (DP) é: >>>>> {verificar}')
    print(f'A soma dos valores da Diagonal Secundária (DS) é: >>>> {analisar}')
    print(f'A soma dos demais valores sem os da DP e DS é: >>>>>>> {calcular}')
    print('=='*30)


def diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                soma += matriz[i][j]  
    return soma


def diagonal_secundaria(matriz):
    somatorio = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i + j == len(matriz)-1:
                somatorio += matriz[i][j]
    return somatorio


def soma_demais_valores(matriz):
    soma_valores = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma_valores += matriz[i][j]
    
    dp = diagonal_principal(matriz)
    ds = diagonal_secundaria(matriz)
    if len(matriz) % 2 != 0:
        valor = (len(matriz) - 1) // 2
        i = j = valor
        aij = matriz[i][j]
        soma = dp + ds - aij
    else:
        soma = dp + ds
    resultado = soma_valores - soma
    return resultado

main()
