def main():

    arquivo = open('words.txt')
    letras_proibidas = str(input('Digite uma sequencia de letras: '))

    total_palavras = 0
    for linha in arquivo:
        palavra = linha.strip()
        analisar = avoids(palavra, letras_proibidas)
        if analisar == True:
            print(palavra)
            total_palavras += 1

    print(f'Total de palavras sem as letras proibidas: {total_palavras}')

    arquivo.close()


def avoids(palavras, letras):
    for i in letras:
        if i in palavras:
            return False
    
    return True

main()
