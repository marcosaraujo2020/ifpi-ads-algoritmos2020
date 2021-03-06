def main():
    menu = '============ OPERAÇÕES COM VETORES ============\n' \
        + ' 1- Inserir novos valores\n' \
        + ' 2- Mostrar valores em posição específica\n' \
        + ' 3- Mostrar todos os valores\n' \
        + ' 4- Remover do Início\n' \
        + ' 5- Remover do Final\n' \
        + ' 6- Remover da Posição Específica\n' \
        + ' 7- Inserir valores em Posição Específica\n' \
        + ' 8- Quantidade de Pares\n' \
        + ' 9- Quantidade de Ímpares\n' \
        + '10- Quantidade de Positivos\n' \
        + '11- Quantidade de Negativos \n' \
        + '12- Média dos Valores \n' \
        + '13- Dobrar todos os valores múltiplos de 2 \n' \
        + '14- Apagar todos os valores.\n' \
        + ' 0- Para sair....\n' \
        + '================================================\n' \
        + 'Opção >>>> '

    vetor = []
    while True:
        opcao = int(input(menu))

        if opcao == 1:
            novos_valores(vetor)
        if opcao == 2:
            posicao_especifica(vetor)
        if opcao == 3:
            todos_valores(vetor)
        if opcao == 4:
            remover_valor_inicio(vetor)
        if opcao == 5:
            remover_valor_final(vetor)
        if opcao == 6:
            remover_posicao_especifica(vetor)
        if opcao == 7:
            inserir_valor_posicao_especifica(vetor)
        if opcao == 8:
            quantidade_pares(vetor)
        if opcao == 9:
            quantidade_impares(vetor)
        if opcao == 10:
            quantidade_positivos(vetor)
        if opcao == 11:
            quantidade_negativos(vetor)
        if opcao == 12:
            media_valores(vetor)
        if opcao == 13:
            multiplos_dois(vetor)
        if opcao == 14:
            limpar_lista(vetor)
        if opcao == 0:
            break
        if opcao < 0 or opcao > 14:
            print('Opção inválida')


def novos_valores(lista):
    quantidade = int(input('Quantidade de valores na lista: '))
    for i in range(quantidade):
        lista.append(int(input(f'Informe {i+1}º valor para a lista: ')))
    
    print('Valores inseridos com sucesso!!!')
    

def posicao_especifica(vetor):
    posicao = int(input('Informe a posição da lista: '))
    if posicao >= 0 and posicao < len(vetor):
        for i in range(len(vetor)):
            if posicao == i:
                print(f'O valor na posição {posicao} da lista é {vetor[i]}')
    else:
        print('Posição inexistente na lista')
        return posicao_especifica(vetor)


def todos_valores(colecao):
    print(f'A lista contém {len(colecao)} valor(es)')
    print(f'Lista = {colecao}')


def remover_valor_inicio(lista_nova):
    print(f'Valor {lista_nova.pop(0)} removido da lista')


def remover_valor_final(novo_vetor):
    print(f'Valor {novo_vetor.pop()} removido da lista')


def remover_posicao_especifica(vetor):
    pos = int(input('Informe a posicao da lista para remover o valor: '))
    if pos >= 0 and pos < len(vetor):
        print(f'O valor {vetor.pop(pos)} da posião {pos} foi removido da lista')
    else:
        print('Posição inexistente na lista')
        return remover_posicao_especifica(vetor)


def inserir_valor_posicao_especifica(nova_colecao):
    posicao = int(input('Informe a posição da lista para inserir valor: '))
    valor = int(input('Qual o valor deseja inserir? '))
    nova_colecao.insert(posicao, valor)
    print(f'O valor {valor} foi inserido na posião {posicao} da lista')


def quantidade_pares(vetor):
    quant_pares = 0
    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            quant_pares += 1
    print(f'A lista contem {quant_pares} números pares')


def quantidade_impares(new_list):
    quant_impares = 0
    for i in range(len(new_list)):
        if new_list[i] % 2 != 0:
            quant_impares += 1
    print(f'A lista contem {quant_impares} números ímpares')


def quantidade_positivos(vetor):
    quant_positivos = 0
    for i in range(len(vetor)):
        if vetor[i] > 0:
            quant_positivos += 1
    print(f'A lista contem {quant_positivos} números positivos')


def quantidade_negativos(vetor):
    quant_negativos = 0
    for i in range(len(vetor)):
        if vetor[i] < 0:
            quant_negativos += 1
    print(f'A lista contem {quant_negativos} números negativos')


def media_valores(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    media = soma / len(vetor)
    print(f'A média dos valores da lista é: {media}')


def multiplos_dois(vetor):
    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            vetor[i] = vetor[i] * 2

def limpar_lista(colecao_nova):
    del colecao_nova[:]


main()
