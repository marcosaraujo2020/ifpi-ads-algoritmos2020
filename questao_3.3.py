def repeticoes(l,b):
    l()
    b()
    b()
    b()
    b()

def linha():
    print('+ - - - - + - - - - +')

def barra():
    print('|         |         |')

def grade():
    repeticoes(linha, barra)
    repeticoes(linha, barra)
    linha()

grade()


#print('+','-'*4,'+','-'*4,'+')

#print('|', ' ' * 4, '|', ' ' * 4, '|')