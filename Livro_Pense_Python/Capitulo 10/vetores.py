def main():
    quantidade_numeros = int(input('Quantos números deseja informar? '))

    vetor = vetor_padrao(quantidade_numeros, -1)
    print(f'Vetor padrão: {vetor}')

    i = 0
    lista = []
    while i < quantidade_numeros:
        lista.append(int(input('Informe um numero: ')))
        i += 1
    
    analisar = pares_impares(lista)
   
    print(f'<<<< Lista numérica formada >>>> {lista}')
    print(f'Nessa lista temos {analisar[0]} números pares e {analisar[1]} números ímpares.')

    verificar = positivo_negativo(lista)
    print(f'Nessa lista temos {verificar[0]} números positivos e {verificar[1]} números negativos.')

    nova_lista = mudar_lista(lista)
    print(f'<<<< Nova lista >>>> {nova_lista}')

    analisar = pares_impares(nova_lista)
    print(f'Na nova lista temos {analisar[0]} números pares e {analisar[1]} números ímpares.')

    verificar = positivo_negativo(nova_lista)
    print(f'Na nova lista temos {verificar[0]} números positivos e {verificar[1]} números negativos.')

    media = media_nova_lista(nova_lista)
    print(f'A média dos valores é {media}')
    print('='*60)
    print()
    


def vetor_padrao(numero, valor):
    lista_padrao = [valor] * numero
    return lista_padrao


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
    pos = 0
    neg = 0
    for valor in lista:
        if valor > 0:
            pos += 1
        elif valor < 0:
            neg += 1
    return pos, neg


def mudar_lista(lista):
    for i in range(len(lista)):
        if lista[i] > 0:
            lista[i] = lista[i] * 2
        elif lista[i] < 0:
            lista[i] = lista[i] / 2
    return lista


def media_nova_lista(nova_lista):
    soma_valores = 0
    for valor in nova_lista:
        soma_valores += valor
    
    media = soma_valores / len(nova_lista)

    return media
    
print()
print('='*60)
main()
