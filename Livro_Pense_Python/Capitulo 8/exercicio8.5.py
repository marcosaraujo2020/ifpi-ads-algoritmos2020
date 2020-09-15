def main():
    palavra = str(input('Escreva uma palavra: '))
    valor = int(input('Digite um valor inteiro: '))

    criptografia = rotacionar(palavra, valor)

    print(f'Mensagem .............: {palavra}')
    print(f'Mensagem criptografada: {criptografia}')


def rotacionar(frase, numero):
    i = 0
    new_word = ''
    while i < len(frase):
        letra = frase[i]
        ordem = ord(letra)
        nova_letra = ordem + numero
        #new_letter = chr(nova_letra)
        new_letter = letras(nova_letra)
        new_word += new_letter
        i += 1
    return new_word


def letras(valor_ordem):
    if (valor_ordem >= 65) and (valor_ordem <= 90) or (valor_ordem >= 97) and (valor_ordem <= 122):
        return chr(valor_ordem)
    elif (valor_ordem > 65) and (valor_ordem < 97) or (valor_ordem > 122) and (valor_ordem < 149):
        return chr(valor_ordem - 26)

main()
