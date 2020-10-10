def main():
    valor = int(input('Quantos valores deseja na lista? '))
    vetor = []
    i = 0
    while i < valor:
        vetor.append(int(input('Informe um numero para a lista: ')))
        i += 1
    analisar = verificar_elementos(vetor)
    print(f'Lista de números >> {vetor}')
    if analisar == True:
        print('Nessa lista contém elementos iguais')
    else:
        print('Não contém elementos iguais na lista')


def verificar_elementos(lista):
    i = 0
    while i < len(lista):
        item = lista[i]
        for c in range(i + 1, len(lista)):
            if lista[c] == item:
                return True
        i += 1
         
main()
