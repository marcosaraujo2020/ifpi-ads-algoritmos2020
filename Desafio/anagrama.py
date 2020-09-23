def main():
    palavra = str(input('Escreva uma palavra em letras minúsculas: '))
    cont = 0
    for letra in range(len(palavra)):
        cont = 0
        if palavra[letra] == 'a':
            cont += 1
    print(f'temos {cont} letras "a"')
        
       

   



main()
