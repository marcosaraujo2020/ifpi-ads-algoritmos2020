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

    print('=='*15)
    for i in matriz:
        print(i)

    simetria = verificar_simetria(matriz)
    
    if simetria == True:
        print('Matriz simétrica')
    else:
        print('Matriz Não simétrica')
    print('=='*15)

def verificar_simetria(transposta):   
    for i in range(len(transposta)):
        for j in range(len(transposta[i])):
            if i != j:
                if transposta[i][j] == transposta[j][i]:
                    return True
                    
main()
