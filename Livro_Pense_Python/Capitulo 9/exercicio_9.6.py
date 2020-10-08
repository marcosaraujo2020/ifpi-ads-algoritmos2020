def main():

    arquivo = open('words.txt')
    total_palavras = 0
    for linha in arquivo:
        palavra = linha.strip()
        verificar = is_abecedarian(palavra)
        if verificar == True:
            print(palavra)
            total_palavras += 1

    print(f'Total de palavras formadas com letras em ordem alfabética: {total_palavras}')

    arquivo.close()


def is_abecedarian(palavra):
    letra = palavra[0]
    for i in palavra:
        if i < letra:
            return False
        letra = i
    return True
  
main()
