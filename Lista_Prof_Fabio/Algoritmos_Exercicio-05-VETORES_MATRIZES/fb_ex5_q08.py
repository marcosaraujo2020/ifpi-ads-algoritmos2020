def main():
    quantidade = int(input('Informe a quantidade de numeros para vetor: '))
    i = 0
    vetor = []
    while i < quantidade:
        vetor.append(int(input(f'Digite um valor a inserir na posição {i} da lista: ')))
        i += 1
    
    print('=='*20)
    verificar = maior_menor(vetor)
    print(f'O maior valor é {verificar[0]} na posção {verificar[1]} \n' \
        + f'O menor valor é {verificar[2]} na posição {verificar[3]}')
    print('=='*20)


def maior_menor(lista):
    maior = 0
    menor = 0
    for c, v in enumerate(lista):
        if c == 0:
            maior = menor = v
        else: 
            if v > maior:
                maior = v
                index_maior = c
            if v < menor:
                menor = v
                index_menor = c
    
    return maior, index_maior, menor, index_menor

main()
