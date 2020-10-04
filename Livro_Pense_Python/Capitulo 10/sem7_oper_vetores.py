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
        + '11- Média dos Valores \n' \
        + '12- Contar ocorrências de um dado valor \n' \
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
    for i in range(len(vetor)):
        if posicao == i:
            print(f'O valor da posição {posicao} da lista é {vetor[i]}')


def todos_valores(colecao):
    print(f'A lista contém {len(colecao)} valor(es)')
    print(f'Lista = {colecao}')


def remover_valor_inicio(lista_nova):
    print(f'Valor {lista_nova.pop(0)} removido da lista')


def remover_valor_final(novo_vetor):
    print(f'Valor {novo_vetor.pop()} removido da lista')


def remover_posicao_especifica(vetor):
    pos = int(input('Informe a posicao da lista para remover o valor: '))
    print(f'O valor {vetor.pop(pos)} da posião {pos} foi removido da lista')


def inserir_valor_posicao_especifica(nova_colecao):
    posicao = int(input('Informe a posição da lista para inserir valor: '))
    valor = int(input('Qual o valor deseja inserir? '))
    nova_colecao.insert(posicao, valor)
    print(f'O valor {valor} foi inserido na posião {posicao} da lista')


main()
