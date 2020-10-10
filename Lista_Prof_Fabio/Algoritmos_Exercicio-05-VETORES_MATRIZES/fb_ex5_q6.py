def main():
    
    numero_binario = str(input('Informe um número binário com 8 bits: '))
    vetor = []
    for i in numero_binario:
        vetor.append(int(i))

    hexadecimal = converter_hexadecimal(vetor)
    print(f'O número Binário {numero_binario} corresponde ao número Hexadecimal {hexadecimal}')

   # decimal = converter_decimal(vetor)
   # print(f'O número Binário {numero_binario} corresponde ao número Decimal {decimal}')


def converter_hexadecimal(lista):
    nova_lista = []
    nova_lista.append(lista[:4])
    nova_lista.append(lista[4:])   
    tam = len(nova_lista)
    c = 0
    while c < tam:  
        termo = ''
        for i in range(tam):
            exp = len(nova_lista[c]) - 1
            soma = 0
            for j in range(len(nova_lista[c])):
                valor = nova_lista[i][j] * 2 ** exp
                soma += valor
                exp -= 1
            
            if soma >=0 and soma < 10:
                termo += str(soma)
            else:
                termo += analisar_hexadecimal(soma)     
            
            c += 1
        return termo


def analisar_hexadecimal(valor):
    resultado = valor + 55
    return chr(resultado)
            
         


'''
def converter_decimal(lista):
    soma = 0
    i = len(lista) - 1
    for v in lista:
        valor = v * 2 ** i
        soma += valor
        i -= 1
    return soma
'''


main()

'''
if soma >=0 and soma < 10:
                termo += str(soma)
            if soma == 10:
                termo += 'A'
            if soma == 11:
                termo += 'B'
            if soma == 12:
                termo += 'C'
            if soma == 13:
                termo += 'D'
            if soma == 14:
                termo += 'E'
            if soma == 15:
                termo += 'F'
'''
