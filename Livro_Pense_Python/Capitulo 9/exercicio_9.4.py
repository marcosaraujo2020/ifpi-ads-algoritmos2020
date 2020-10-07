def main():

    arquivo = open('words.txt')
    serie_letras = str(input('Digite uma série de letras: '))

    total_palavras = 0
    for linha in arquivo:
        palavra = linha.strip()
        verificar = uses_only(palavra, serie_letras)
        if verificar == True:
            print(palavra)
            total_palavras += 1

    print(f'Total de palavras com as serie de letras informadas: {total_palavras}')

    arquivo.close()


def uses_only(palavras, letras):
    for i in letras:
        if i not in palavras:
            return False
   
    return True

main()
