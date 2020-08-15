def main():
   print('A seguir informe duas datas no formato DD-MM-AAAA: ')
   print('Para a primeira data digite os na ordem')
   dia1 = int(input('Dia 1: '))
   mes1 = int(input('Mes 1: '))
   ano1 = int(input('Ano 1: '))
   print('Para a segunda data informe')
   dia2 = int(input('Dia 2: '))
   mes2 = int(input('Mes 2: '))
   ano2 = int(input('Ano 2: '))

   analisar_data(dia1, mes1, ano1, dia2, mes2, ano2)

def analisar_data(d1, m1, a1, d2, m2, a2):
    if d1 == d2 and m1 == m2 and a1 == a2:
        status1(d1, m1, a1)
    elif a1 > a2 or a1 == a2 and m1 > m2 or a1 == a2 and m1 == m2 and d1 > d2:
        status2(d1, m1, a1)
    elif a1 < a2 or a1 == a2 and m1 < m2 or a1 == a2 and m1 == m2 and d1 < d2:
        status2(d2, m2, a2)

    elif a1 == a2 and m1 < m2:
        status2(d2, m2, a2)

def status1(x, y, z):
    print(f'As datas são iguais: {x}/{y}/{z}')

def status2(x, y, z):
    print(f'A data {x}/{y}/{z} é mais recente')

main()