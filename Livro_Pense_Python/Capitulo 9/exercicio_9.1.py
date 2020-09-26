def main():
    
    fin = open('words.txt')
    
    cont = 0
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)
            cont += 1
    print(f'Encontradas {cont} palavras.')

    fin.close()

main()
