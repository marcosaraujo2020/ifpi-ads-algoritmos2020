hora_inicio = int(input('Digite a hora do inicio do jogo: '))
minutos_inicio = int(input('Digite os minutos de inicio do jogo: '))
hora_final = int(input('Digite a hora do final do jogo: '))
minutos_final = int(input('Digite os minutos finais do jogo: '))

total_minutos_inicio = hora_inicio * 60 + minutos_inicio
total_minutos_final = hora_final * 60 + minutos_final
tempo_total_minutos = total_minutos_final - total_minutos_inicio

if tempo_total_minutos > 0:

    duracao_hora = tempo_total_minutos // 60
    duracao_minutos = tempo_total_minutos % 60

    print(f'Inicio do Jogos: {hora_inicio}:{minutos_inicio} h')
    print(f'Final do Jogos: {hora_final}:{minutos_final} h')
    print('')
    print(f'A duração do jogo foi de {duracao_hora} horas e {duracao_minutos} minutos.')
else:
    tempo_total_minutos = 1440 + total_minutos_final - total_minutos_inicio


    duracao_hora = tempo_total_minutos // 60
    duracao_minutos = tempo_total_minutos % 60

    print(f'Inicio do Jogos: {hora_inicio}:{minutos_inicio} h')
    print(f'Final do Jogos: {hora_final}:{minutos_final} h')
    print('')
    print(f'A duração do jogo foi de {duracao_hora} horas e {duracao_minutos} minutos.')