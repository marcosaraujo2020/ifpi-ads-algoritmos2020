print('-=' * 25)
print('EMPRESA LINUX LTDA')
print('-=' * 25)

def main():
    matricula = int(input('Número da matrícula: '))
    horas_trabalhadas = int(input('Quantidade de Horas trabalhadas? '))
    dependentes = int(input('Números de dependentes: '))
    Vencimento = horas_trabalhadas * 12 
    salario_familia = dependentes * 40
    salario_bruto = Vencimento + salario_familia
    inss = salario_bruto * 0.085
    ir = salario_bruto * 0.05
    descontos = ir + inss
    salario_liquido = salario_bruto - descontos

    print('=='*25)
    print('CONTRA CHEQUE')
    print('=='*25)
    print('LANÇAMENTOS')
    print('')
    print(f'Vencimento ....................... R$ {Vencimento:.2f}')
    print(f'Salário família................... R$ {salario_familia:.2f}')
    print('')
    print('')
    print('')
    print('=='*25)
    print('DESCONTOS')
    print('')
    print(f'Previdencia-INSS.................. R$ {inss:.2f}')
    print(f'Imposto de Renda ................. R$ {ir:.2f}')
    print('=='*25)
    print(f'Salário Bruto: R$ {salario_bruto:.2f} | Descontos: R$ {descontos:.2f}')
    print('--'*25)
    print(f'Salário Líquido: R$ {salario_liquido:.2f}')
    print('=='*25)
    print('')

main()
