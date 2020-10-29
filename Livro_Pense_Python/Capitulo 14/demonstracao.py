def main():
    
    frutas = list()

    arquivo = open('frutas.txt', 'r')

    for fruta in arquivo:
        frutas.append(fruta.strip())

    print(frutas)
    
    arquivo.close()

main()
