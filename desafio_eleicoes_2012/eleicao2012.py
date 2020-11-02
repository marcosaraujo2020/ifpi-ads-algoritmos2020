import os
import json

# Atividade em edição ainda .... 01/11/2020 
# Organizando as ideias ... 

def main():

    #part_colig = inicializar('coligacoes.bd')

    arquivo1 = open('partidos_coligacoes_the_2012.csv')
    arquivo2 = open('candidatos_e_votos_vereador_THE_2012.csv')
 
    coligacoes = list()
    candidatos = list()
    
    # Para criar dict com cada coligação e informações iniciais
    for linha in arquivo1:
        coligacao = dict()
        coligacao['coligacao'] = linha.strip()
        coligacao['total_votos'] = 0
        coligacao['qtd_vagas'] = 0
        coligacao['votos_sobra_total'] = 0
        coligacoes.append(coligacao)

    # Lista matriz com vetores de vereadores e informações convertidas do arquivo2.csv
    matriz = list()
    for linha in arquivo2:
        lin = linha.split(";")
        matriz.append(lin)

    # Acessa o vetor da matriz e gera dicionario com cada vereador e informações
    tot_votos = 0
    for i in range(len(matriz)):
        candidato = dict()
        candidato['nome'] = matriz[i][0]
        candidato['numero'] = matriz[i][1]
        candidato['partido'] = matriz[i][2]
        candidato['coligacao'] = matriz[i][3]
        candidato['total_votos'] = matriz[i][4].strip()
        tot_votos += int(matriz[i][4].strip())
        candidatos.append(candidato)

    menu = menu_principal()
    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            votos_coligacao(coligacoes, candidatos)
        if opcao == 2:
            votos_por_vereador(candidatos)
        if opcao == 3:
            pass
            #consultar_por_vereador(candidatos)
        if opcao == 4:
            votos = votos_coligacao(coligacoes, candidatos)
            valor_tot = votos_total_eleicao(candidatos)
            vagas_por_coligacao(votos, valor_tot)
        if opcao == 5:
            votos_total_eleicao(candidatos)
        if opcao == 6:
            total_candidatos(candidatos)
        if opcao < 0 or opcao > 6:
            print('Opção inválida! Tente novamente')
        
        print()
        input('Tecle <<enter>> para continuar.... \n')
        opcao = int(input(menu))

    #part_colig.append(coligacoes)
    arquivo1.close()
    arquivo2.close()
    #finalizar('coligacoes.bd', part_colig)


def menu_principal():
    menu = '============================================== \n'
    menu += '         TSE Eleições 2012 - Teresina \n'
    menu += '============================================== \n'
    menu += '1 - Mostrar votos por coligação \n'
    menu += '2 - Listar votos dos candidatos \n'
    menu += '3 - Consultar vereador por nome ou numero \n'
    menu += '4 - Consultar vagas por coligação \n'
    menu += '5 - Consultar total de votos da eleição \n'
    menu += '6 - Consultar total de candidatos na disputa \n'
    menu += '0 - Encerrar aplicativo \n'
    menu += '============================================== \n'
    menu += 'Digite uma opção >> '
    
    return menu

#Contabilizar votos de partidos ou coligação
def votos_coligacao(coligacoes, candidatos):
    lista_coligacoes = list()
    valores = list()
    for chave in coligacoes:
        votos_coligacao = dict()
        votos_partido = 0
        for vereador in candidatos:
            if chave['coligacao'] == vereador['coligacao']:
                votos = int(vereador['total_votos'])
                votos_partido += votos
        votos_coligacao['coligacao'] = chave['coligacao']
        votos_coligacao['quant_votos'] = votos_partido
        valores.append(votos_partido)

        lista_coligacoes.append(votos_coligacao)
    
    resultado = ordenar_valores(valores, lista_coligacoes)

    print('----------------------------------------------')
    print(f'{"Partido/Coligação":>20}  | {"Total de votos":>15}')
    print('----------------------------------------------')
    for i in range(len(resultado)):
        print(f'{resultado[i]["coligacao"]:>20} = {resultado[i]["quant_votos"]:>8}')
    print('----------------------------------------------')

    return lista_coligacoes

# Lista votos por vereador
def votos_por_vereador(candidatos):
    print('----------------------------------------------')
    print(f'{"Nome":>20}           | {"Nº de votos":>8}')
    print('----------------------------------------------')
    for vereador in candidatos:
        print(f'{vereador["nome"]:>30} = {vereador["total_votos"]:>5}')
    print('----------------------------------------------')


def votos_total_eleicao(candidatos):
    votos_total = 0
    tam = len(candidatos)
    for i in range(tam):
        n_voto = int(candidatos[i]['total_votos'])
        votos_total += n_voto

    print('----------------------------------------------')
    print(f'Total de votos válidos da eleiçao: {votos_total}')
    print('----------------------------------------------')

    return votos_total

def vagas_por_coligacao(votos_partidos, valor_tot):
    quociente_eleitoral = valor_tot // 29       
    vagas_partidos = list()
    for i in votos_partidos:
        vagas_colig = dict()
        for v in i:
            quociente_partidario = i['quant_votos'] // quociente_eleitoral
        
        vagas_colig['coligacao'] = i['coligacao']
        vagas_colig['quant_vagas'] = quociente_partidario
        vagas_partidos.append(vagas_colig)

    print('----------------------------------------------')
    print(f'{"Partido/Coligação":>20}  | {"Nº de vagas":>15}')
    print('----------------------------------------------')
    tot = 0
    for i in range(len(vagas_partidos)):
        print(f'{vagas_partidos[i]["coligacao"]:>20} = {vagas_partidos[i]["quant_vagas"]:>8}')
        tot += vagas_partidos[i]['quant_vagas']
    
    print()
    print(f'{"Total de vagas":>20} = {tot:>8}')
    print('----------------------------------------------')



def total_candidatos(candidatos):
    tot_cand = len(candidatos)
    print('----------------------------------------------')
    print(f'Total de candidatos na disputa eleitoral: {tot_cand}')
    print('----------------------------------------------')


def ordenar_valores(valores, lista_coligacoes):
    valores.sort(reverse=True)
    nova_lista = list()
    for v in valores:
        novo_dicionario = dict()
        for num in lista_coligacoes:
            if v == num['quant_votos']:
                novo_dicionario['coligacao'] = num['coligacao']
                novo_dicionario['quant_votos'] = v
        nova_lista.append(novo_dicionario)

    return nova_lista
    
'''
# INICIO DO ARQUIVO
def inicializar(arquivo):
    coligacoes = list()
    if os.path.exists(arquivo):
        arq = open(arquivo)
        dados = arq.readline()
        arq.close()

        if dados:
            coligacoes = json.loads(dados)
    return coligacoes

# FECHAMENTO DO ARQUIVO
def finalizar(arquivo, part_colig):
    dados = json.dumps(part_colig)
    arq = open(arquivo, 'w')
    arq.write(dados)
    arq.close()
'''

main()
