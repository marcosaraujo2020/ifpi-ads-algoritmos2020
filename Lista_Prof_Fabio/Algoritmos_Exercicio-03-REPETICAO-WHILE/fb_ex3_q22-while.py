def main():
    maior = menor = 0
    ficha_menor = 0
    ficha_maior = 0
    fazendeiro1 = ' '
    fazendeiro2 = ' '
    resposta = ' '
    while resposta not in 'N':
        numero_ficha = int(input('Informe o número da ficha (5 dígitos): '))
        nome = str(input('Nome do fazendeiro: ')).title()
        peso = float(input('Peso do Boi: '))
          
        if peso > maior:
            maior = menor = peso
            ficha_maior = numero_ficha
            fazendeiro1 = nome
        elif peso < menor:
            menor = peso
            ficha_menor = numero_ficha
            fazendeiro2 = nome
        
        resposta = str(input('Deseja continuar cadastrando? [S/N] ')).upper().split()[0]
        if resposta == 'N':
            break
        
    print('')
    print('---' * 20)
    print(f'Número de identificação: \033[1;33m{ficha_maior}\033[m')
    print(f'Nome do Fazendeiro: \033[1;33m{fazendeiro1}\033[m')
    print(f'Boi mais gordo: \033[1;33m{maior} Kg\033[m')
    print('---' * 20)
    print(f'Número de identificação: \033[1;31m{ficha_menor}\033[m')
    print(f'Nome do Fazendeiro: \033[1;31m{fazendeiro2}\033[m')
    print(f'Boi mais magro: \033[1;31m{menor} Kg\033[m')
    print('---' * 20)
    print('')

main()