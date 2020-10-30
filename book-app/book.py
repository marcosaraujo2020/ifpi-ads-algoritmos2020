import os
import json

def main():
    libros = inicializar('livros.bd')   #.bd é uma lista com dicionário
    menu = tela_opcoes()
    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            livro = novo_livro()
            libros.append(livro)
        elif opcao == 2:
            conferir_livros = listar_livros(libros)
        elif opcao == 3:
            busca = consultar_livros(libros)
        print()
        input('tecle <<enter>> para continuar... \n')
       
        opcao = int(input(menu))

    finalizar('livros.bd', libros)

# Menu Principal
def tela_opcoes():
    menu = '======= App Book ======= \n' \
        + '1 - Cadastrar novo livro \n' \
        + '2 - Listar Livros \n' \
        + '3 - Consultar Livros \n' \
        + '0 - Finalizar Aplicativo \n' \
        + '======================== \n' \
        + 'opção >>> '
    return menu

# Cadastrar um novo livro no bd
def novo_livro():
    print('<< Preencha os dados para cadastrar novo livro >> \n')
    nome = str(input('Nome do livro: ')).title()
    editora = str(input('Editora: ')).title()
    volume = str(input('Volume: ')).capitalize()
    ano = int(input('Ano de publicação: '))
    valor = float(input('Qual o valor? R$ '))
    digital = str(input('Livro digital? [Sim/Nao] ')).capitalize()
    quant_autor = int(input('Quantos autores tem esse livro? '))
    autores = list()
    
    for i in range(quant_autor):
        autor = str(input(f'Nome do {i+1}º autor? ')).title()
        autores.append(autor)
    
    livro = {'nome': nome, 'editora': editora, 'volume': volume, 'ano': ano,
            'valor': valor, 'digital': digital, 'autores': autores}

    print('Livro cadastrado!')
    return livro

# Exibir os livros cadastrados
def listar_livros(colecao):
    quant = len(colecao)
    print('===== Confira a coleção de nossos livros ===== \n')
    print(f'Temos {quant} livros disponíveis')

    for item in colecao:
        print('---'*15)
        for chave in item:
            print(f'\t{chave.capitalize()}:', item[chave])       
    print('---'*15)

# Faz busca por livros 
def consultar_livros(books):
    print('----'*15)
    print('                      Iniciar pesquisa                      ')
    print('----'*15)
    search = str(input('Informe o nome do livro ou da editora: ')).title()
    
    livros_localizados = list()
    tam = len(books)
    for c in range(tam):  
        for valor in books[c].values():
            if search == valor:
                livros_localizados.append(books[c])
    
    quant = len(livros_localizados)
    for i in range(quant):
        print(f'Livro nº {i+1}:', livros_localizados[i]['nome'])

    print()
    print(f'Total de livros localizados: {quant}')
    print('----'*15)

    while True:
        cod = int(input('Selecione o livro que deseja pelo nº ou [999 parar]: '))
        if cod == 999:
            break
        elif cod <= 0 or cod > quant:
            print(f'ERRO! Não existe livro com o nº {cod} na lista! Tente novamente')
        else:
            exibir_menu = tela_lista(livros_localizados[cod-1], livros_localizados[cod-1]['nome'], cod)
        
    
def tela_lista(dict_livro, nome, cod):
    menu2 = f'======= Livro de {nome} Selecionado ======= \n' \
        + '1 - Exibir detalhes \n' \
        + '2 - Remover livro \n' \
        + '3 - Editar informações \n' \
        + '4 - Duplicar registro \n' \
        + '0 - Finalizar \n' \
        + '============================================ \n' \
        + 'opção >>> '
    
    opcao = int(input(menu2))
    while opcao != 0: 
        if opcao == 0:
            break
        if opcao == 1:
            detalhar = detalhar_livro(dict_livro)
        if 1 < opcao <= 4:
            print('Função ainda não definida...')
        if opcao < 0 or opcao > 4:
            print('Opção inválida! Tente novamente')
            
        print()
        input('tecle <<enter>> para continuar... \n')
        opcao = int(input(menu2))

# Exibir detalhes do livro escolhido
def detalhar_livro(livro):
    for k, v in livro.items():
            print(f'\t{k.capitalize()}:', livro[k])
    print('============================================')

# Listar todos os livros cadastrados
def exibir_livro(colecao_livros):
    quant = len(colecao_livros)
    print()
    print(f'>> Foram encontrados {quant} livros')
    print('----'*15)
    
    for i in range(quant):
        print(f'Livro Nº: {i+1}')
        for chave in colecao_livros[i]:
            print(f'\t{chave.capitalize()}:', colecao_livros[i][chave]) 
    
        print('----'*15)

# INICIO DO ARQUIVO
def inicializar(arquivo):
    livros = list()
    if os.path.exists(arquivo):
        arq = open(arquivo)

        dados = arq.readline()
        arq.close()

        if dados:
            livros = json.loads(dados)

    return livros

# FECHAMENTO DO ARQUIVO
def finalizar(arquivo, libros):
    dados = json.dumps(libros)
    arq = open(arquivo, 'w')
    arq.write(dados)
    arq.close()

main()
