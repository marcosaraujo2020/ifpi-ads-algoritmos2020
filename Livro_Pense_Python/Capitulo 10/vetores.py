def main():
    quantidade_numeros = int(input('Quantos números deseja informar? '))
    i = 0
    lista = []
    while i < quantidade_numeros:
        lista.append(int(input('Informe um numero: ')))
        i += 1
    analisar = pares_impares(lista)
   
    print(f'Lista numérica formada >> {lista}')
    print(f'Nessa lista temos {analisar[0]} números pares e {analisar[1]} números ímpares.')

    verificar = positivo_negativo(lista)

    print(f'Nessa lista temos {analisar[0]} números positivos e {analisar[1]} números negativos.')



def pares_impares(lista):
    pares = 0
    impares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares



def positivo_negativo(lista):
    pos = neg = 0
    for i in range(len(lista)):
        if lista[i] >= 0:
            pos += 1
        elif lista[i] < 0:
            neg += 1
    return pos, neg

       
# falta concluir e ...


main()
