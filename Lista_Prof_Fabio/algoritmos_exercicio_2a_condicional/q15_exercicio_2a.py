def main():
    print('Digite a seguir a quantidade de hora/aula e valor da hora/aula de dois professores')
    professorA = str(input('Qual o nome do(a) Professor(a) A: '))
    professorB = str(input('Qual o nome do(a) Professor(a) B: '))
    hora_profA = int(input('Digite a quantidade de hora/aula Professor(a) A: '))
    hora_profB = int(input('Digite a quantidade de hora/aula Professor(a) B: '))
    valor_ha_profA = float(input('Qual o valor da hora/aula Professor(a) A: R$ '))
    valor_ha_profB = float(input('Qual o valor da hora/aula Professor(a) B: R$ '))

    salario_maior(professorA, professorB, hora_profA, hora_profB, valor_ha_profA, valor_ha_profB)

def salario_maior(profA, profB , x, y, z, w):
    salario_profA = x * z
    salario_profB = y * w

    if salario_profA > salario_profB:
        print('{} tem o maior salário de R$ {:.2f} reais.'.format(profA, salario_profA))
    elif salario_profA < salario_profB:
        print('{} tem o maior salário de R$ {:.2f} reais.'.format(profB, salario_profB))
    else:
        print('{} e {} recebem o mesmo salário de R$ {:.2f} reais.'.format(profA, profB, salario_profA))

main()
