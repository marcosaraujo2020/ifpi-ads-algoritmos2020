print('='*20)
print('Equação do 2º Grau')
print('='*20)

def main():

    print('Informe valores para os coeficientes A, B e C da equação do 2º grau')
    A = float(input('Coeficiente A: '))
    B = float(input('Coeficiente B: '))
    C = float(input('Coeficiente C: '))

    equacao_grau2(A, B, C)
    raizes = equacao_grau2(A, B, C)
    print(f'A expressão {A:.0f}x² + {B:.0f}x + {C:.0f} = 0 \n {raizes}')

def equacao_grau2(a, b, c):
    if a == 0:
        return 'Não é uma equação do 2º grau.'
    elif a != 0 and b != 0 and c != 0:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return 'não admite solução real'
        elif delta > 0:
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)
            return f'tem raízes reais {x1:.1f} e {x2:.1f}'
        elif delta == 0:
            x = - b / (2 * a)
            return f'tem raiz real {x:.1f}'
    elif a != 0 and b == 0 and c != 0:
        x = (c / a) ** 0.5
        return f'tem raiz real {x:.1f}'
    elif a != 0 and b != 0 and c == 0:
        x1 = 0
        x2 = - b / a
        return f'tem raízes reais {x1:.1f} e {x2:.1f}'
    elif a != 0 and b == c == 0:
        return 'raiz real é zero'

main()

