from time import sleep
from random import randint

def cabeçalho():
    titulo = 'CONSÓRCIO ENTRE AMIGOS'
    tam = len(titulo) + 6
    print('=' * tam)
    print(f'   {titulo}')
    print('=' * tam)

    grupo_consorcio()


def grupo_consorcio():
    grupo = ['Ana Lúcia', 'Cardoso', 'Evania', 'Frances', 'Gilmara', 'Hilton', 'Joana', 'Marcos', 'Mariane', 'Rejane']
    print(' \033[32mParticipantes do consórcio:\033[m')
    print('-' * 28)
    for pessoa in grupo:
        print(pessoa)
    print()
    print(f'Total de \033[36m{len(grupo)}\033[m pessoas')
    print('-' * 28)

    sorteio(grupo)


def sorteio(lista):
    print('    \033[35mIniciando o Sorteio!\033[m')
    print('-'*28)
    tam = len(lista)
    
    cont = 0
    
    while cont <= tam:
        tot = 0
        premiados = list()
        while True:
            numeros = randint(0, tam-1)
            if numeros not in premiados:
                premiados.append(numeros)
                tot += 1
            if tot >= tam:
                break

        cont += 1

    listar(premiados, lista)


def listar(membros, lista):
    print('         \033[36mBoa Sorte!\033[m')
    print('-' * 28)
    for i in range(len(membros)):
        sleep(1)
        print(f'{i+1:>2}º mês - \033[33m{lista[membros[i]]}\033[m')
    print('-' * 28)
    print('         \033[36mObrigado!\033[m')
    print('-' * 28)
    print()


cabeçalho()
