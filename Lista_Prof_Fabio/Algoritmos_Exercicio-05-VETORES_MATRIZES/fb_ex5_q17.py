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

    calcular = linha_maior_menor_soma(matriz)
    print(calcular)


def linha_maior_menor_soma(matriz):
    maior = 0
    menor = 0
    for i in range(len(matriz)):
           
        soma = 0
        for j in range(len(matriz[i])):
            soma += matriz[i][j]      
        
        if i == 0:
            maior = menor = soma
        else:
            if soma > maior:
                maior = soma
                linha_maior = i
            if soma < menor:
                menor = soma
                linha_menor = i
                
    return maior, linha_maior, menor, linha_menor


main()
