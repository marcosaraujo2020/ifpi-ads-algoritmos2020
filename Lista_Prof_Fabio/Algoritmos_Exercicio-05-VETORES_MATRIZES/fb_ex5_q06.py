def main():
    numero_binario = str(input('Informe um número binário com 8 bits: '))
    vetor = []
    for i in numero_binario:
        vetor.append(int(i))

    hexadecimal = converter_hexadecimal(vetor)
    decimal = converter_decimal(vetor)

    print('=='*20)
    print(f'O número Binário {numero_binario} equivale ao: \n' \
        + f'Número Hexadecimal >> {hexadecimal}\n' \
        + f'Número Decimal >>>>>> {decimal}')
    print('=='*20)


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
            

def converter_decimal(lista):
    soma = 0
    i = len(lista) - 1
    for v in lista:
        valor = v * 2 ** i
        soma += valor
        i -= 1
    return soma

main()
