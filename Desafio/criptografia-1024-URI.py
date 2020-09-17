def main():
    mensagem = str(input('Escreva uma frase: '))
    
    criptografar = criptografia(mensagem)

    print(f'Mensagem criptografada: {criptografar}')


def criptografia(texto):
    i = 0
    passada_one = ''
    while i < len(texto): 
        letra = texto[i]
        ordem = ord(letra)
        novo_caractere = eh_letra(ordem)
        passada_one += novo_caractere
        i += 1
    
    passada_two = inverter(passada_one)
    passada_three = novo_texto(passada_two)
    
    return passada_three


def eh_letra(caractere):
    if (caractere >= 65) and (caractere <= 90) or (caractere >= 97) and (caractere <= 122):
        return chr(caractere + 3)
    else:
        return chr(caractere)


def inverter(novo_texto):
    palavra = ''
    for c in range(len(novo_texto)-1, -1, -1):
        palavra += novo_texto[c]
    return palavra


def novo_texto(nova_palavra):
    texto_final = ''
    posicao = len(nova_palavra) // 2
    for i in range(len(nova_palavra)):
        if i < posicao:
            texto_final += nova_palavra[i]
        if i >= posicao:
            letra = nova_palavra[i]
            ordem = ord(letra)
            nova_letra = chr(ordem - 1)
            texto_final += nova_letra

    return texto_final

main()

