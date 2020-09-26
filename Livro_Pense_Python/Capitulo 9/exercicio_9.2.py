def main():
    arquivo = open('words.txt')
    
    total_palavras = 0
    total_palavras_sem_e = 0
    for linha in arquivo:
        palavra = linha.strip()
        total_palavras += 1
        palavra_sem_e = has_no_e(palavra)
        if palavra_sem_e == True:
            print(palavra)
            total_palavras_sem_e += 1

    percentual = percentual_palavras_sem_e(total_palavras, total_palavras_sem_e)
    
    print(f'Total de palavras: {total_palavras}')
    print(f'O total de palavras sem a letra "e": {total_palavras_sem_e}')
    print(f'O Percentual de palavras sem a letra "e" é de: {percentual:.2f} %')

    arquivo.close()


def has_no_e(palavra):
    for letra in palavra:
        if letra == 'e':
            return False
    return True


def percentual_palavras_sem_e(total, total_sem_e):
    perc = (total_sem_e / total) * 100
    return perc
   
main()
