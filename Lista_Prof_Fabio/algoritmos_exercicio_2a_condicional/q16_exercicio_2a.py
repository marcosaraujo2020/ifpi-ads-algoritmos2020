nota1 = float(input('Informe a 1º Nota: '))
nota2 = float(input('Informe a 2º Nota: '))

media = (nota1 + nota2) / 2

print('Nota média: {:.1f}'.format(media))

if media >= 7.0:
    print('Aprovado')
else:
    nota_exame = float(input('Digite a nota do exame: '))
    media_final = (media + nota_exame) / 2
    print('Média final: {:.1f}'.format(media_final))

    if media_final >= 5.0:
        print('Aprovado')
    else:
        print('Reprovado')