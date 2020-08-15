# ENTRADA
print('')
print('Resolver o sistema de equações lineares do tipo:')
print('ax + by = c')
print('dx + ey = f')
print('--'*6)
print('Informe os valores dos coeficientes a seguir: ')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
e = int(input('e = '))
f = int(input('f = '))

# PROCESSAMENTO
x = int((c * e - b * f) / (a * e - b * d))
y = int((a * f - c * d) / (a * e - b * d))

# SAÍDA
print('O valores de x e y do sistema de equações são: x = {} e y = {}' .format(x, y))

