import os
import json

# Atividade em edição ainda .... 31/10/2020 
# Organizando as ideias ... 

def main():
    arquivo1 = open('partidos_coligacoes_the_2012.csv')
    arquivo2 = open('candidatos_e_votos_vereador_THE_2012.csv')

    menu = menu_principal()
    opcao = int(input(menu))
 
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
        #print(f'{linha.strip()}') 
    #print(coligacoes)

    # Lista matriz com vetores de vereadores e informações convertidas do arquivo2.csv
    matriz = list()
    for linha in arquivo2:
        lin = linha.split(";")
        matriz.append(lin)


def menu_principal():
    menu = '============================================== \n'
    menu += '         TSE Eleições 2012 - Teresina \n'
    menu += '============================================== \n'
    menu += '1 - Mostrar votos por coligação \n'
    menu += '2 - Consultar vereador por nome ou numero \n'
    menu += '3 - \n'
    menu += '0 - Encerrar aplicativo \n'
    menu += '============================================== \n'
    menu += 'Digite uma opção >> '

    return menu

#Contabilizar votos de partidos ou coligação
def votos_coligacao():
    votos_partido = 0
    for vereador in candidatos: 
        if vereador['coligacao'] == 'PC do B':
            votos = int(vereador['total_votos'])
            votos_partido += votos
    print(f'O partido teve {votos_partido} votos válidos.')


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
    print(candidatos)
    print(f'O total de vereadores é de {len(candidatos)}.')
    print(f'O total de votos válidos de todos os candidatos foram de {tot_votos} votos.')
    
    
    #QE >> Quociente Eleitoral 
    # QE = nt_votos / num_vagas      
    QE = tot_votos // 29
    print(f'O Quociente Eleitoral: {QE}')
    

    #QP >> Quociente Partidario
    #QP = votos_partido / QE         
    #QP = votos_partido // QE
           
    
    


    arquivo1.close()
    arquivo2.close()

# INICIO DO ARQUIVO
""" def inicializar(arquivo):
    candidatos = list()
    if os.path.exists(arquivo):
        arq = open(arquivo)
        dados = arq.readline()
        arq.close()

        if dados:
            candidatos = json.loads(dados)
    return candidatos

# FECHAMENTO DO ARQUIVO
def finalizar(arquivo, cand_vereador):
    dados = json.dumps(cand_vereador)
    arq = open(arquivo, 'w')
    arq.write(dados)
    arq.close() """

main()
