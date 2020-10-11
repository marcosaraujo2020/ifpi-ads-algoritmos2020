def main():
    quantidade = int(input('Informe a quantidade de numeros para vetor: '))
    i = 0
    vetor = []
    while i < quantidade:
        vetor.append(int(input(f'Digite um valor a inserir na posição {i} da lista: ')))
        i += 1
    
    print('=='*20)
    print(f'Vetor = {vetor}')
    print()

    verificar = maior_menor(vetor)
    
    print(f'O maior valor é {verificar[0]} na posção {verificar[1]} \n' \
        + f'O menor valor é {verificar[2]} na posição {verificar[3]}')
    print('=='*20)


def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    index_maior = 0
    index_menor = 0
    for c in range(1, len(lista)):  
        if lista[c] > maior:
            maior = lista[c]
            index_maior = c
        if lista[c] < menor:
            menor = lista[c]
            index_menor = c
    
    return maior, index_maior, menor, index_menor


main()
