def main():
    resposta = 'SN'
    quantidade_pessoas = quantidade_filhos = recebe_ate_mil = somatorio_salario = 0

    while resposta not in 'N':
        salario = float(input('Valor do salário: R$ '))
        numero_filhos = int(input('Quantidade de filhos: '))

        quantidade_pessoas += 1
        quantidade_filhos += numero_filhos
        somatorio_salario += salario
        
        if salario <= 1000:
            recebe_ate_mil += 1 

        resposta = str(input('Desaja continuar coletando dados? [S/N] ')).upper().split()[0]
        if resposta == 'N':
            break
    
    media_salario = somatorio_salario / quantidade_pessoas
    media_filhos = quantidade_filhos / quantidade_pessoas
    percentual_ate_mil = recebe_ate_mil * 100 / quantidade_pessoas

    print('')
    print('+----+' * 10)
    print(f'A média do salário da população: R$ {media_salario:.2f}')
    print(f'A média do número de filhos: {media_filhos:.2f}')
    print(f'Percentual de pessoas com salário de até R$ 1.000 >>> {percentual_ate_mil} %')

    print('+----+' * 10)

main()
