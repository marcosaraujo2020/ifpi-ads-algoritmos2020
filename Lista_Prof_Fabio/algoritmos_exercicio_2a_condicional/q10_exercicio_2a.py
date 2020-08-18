def main():
    print('A seguir digite uma data')
    dia = int(input('Informe dia: '))
    mes = int(input('Informe mês: '))
    ano = int(input('Informe ano: '))

    analisar_ano(dia, mes, ano)

def analisar_ano(d, m, a):
    if d > 31 or d < 0 or m > 12 or m < 0:
        print('Data inexistente!!')

    elif m == 4 or m == 6 or m == 9 or m == 11:
        if 0 < d <= 30:
            print('A data {}/{}/{} é válida!'.format(d, m, a))
        else:
            print('Data inválida')

    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if 0 < d <= 31:
            print('A data {}/{}/{} é válida!'.format(d, m, a))
        else:
            print('Data inválida')

    if m == 2:
        if a % 4 == 0 and a % 100 != 0 or a % 100 == 0 and a % 400 == 0:
            if 0 < d <= 29:
                print('A data {}/{}/{} é válida!'.format(d, m, a))
            else:
                print(f'Data inválida')

        elif a % 4 != 0:
            if 0 < d <= 28:
                print('A data {}/{}/{} é válida!'.format(d, m, a))
            else:
                print(f'Data inválida, {a} não foi ano bissexto.')

main()
