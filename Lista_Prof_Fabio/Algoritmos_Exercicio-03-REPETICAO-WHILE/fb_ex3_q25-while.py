print('==' * 10)
print('Eleição Presidencial')
print('==' * 10)
print('')
print('OPÇÕES DE VOTAÇÃO')
print('1 -- Candidato A')
print('2 -- Candidato B')
print('3 -- Candidato C')
print('9 -- Voto NULO')
print('0 -- Voto BRANCO')
print('==' * 10)
print('')

def main():
    votacao = 'SN'
    candidato_A  = candidato_B = candidato_C = votos_nulo = votos_branco = 0
    while votacao not in 'S':
        codigo = int(input('Digite o códico do candidato: '))
        if codigo == 1:
            candidato_A += 1
        elif codigo == 2:
            candidato_B += 1
        elif codigo == 3:
            candidato_C += 1
        elif codigo == 9:
            votos_nulo += 1
        elif codigo == 0:
            votos_branco += 1
        else:
            print('Código inválido!!')
            return main()
        votacao = str(input('A votação encerrou? [S/N] ')).upper().split()[0]
        if votacao == 'S':
            break

    print('')
    print('==' * 25)
    print('Apuração da eleição ..... Quantidade de Votos')
    print(f'Candidato A: ...................... {candidato_A}')
    print(f'Candidato B: ...................... {candidato_B}')
    print(f'Candidato C: ...................... {candidato_C}')
    print(f'Votos Nulos: ...................... {votos_nulo}')
    print(f'Votos Brancos: .................... {votos_branco}')
    print('==' * 25)
    if candidato_A == candidato_B == candidato_C:
        print('Empate na votação entre os três candidatos!')
    elif candidato_A == candidato_B > candidato_C:
        print('Empate na votação entre os candidatos A e B!')
    elif candidato_A == candidato_C > candidato_B:
        print('Empate na votação entre os candidatos A e C!')
    elif candidato_B == candidato_C > candidato_A:
        print('Empate na votação entre os candidatos B e C!')
    elif candidato_A > candidato_B >= candidato_C:
        print('Candidato A Venceu a Eleição!! Parabéns!')
    elif candidato_A < candidato_B and candidato_B > candidato_C:
        print('Candidato B Venceu a Eleição!! Parabéns!')
    elif candidato_A < candidato_C > candidato_B:
        print('Candidato C Venceu a Eleição!! Parabéns!')
    print('==' * 25)
    print('')
main()
