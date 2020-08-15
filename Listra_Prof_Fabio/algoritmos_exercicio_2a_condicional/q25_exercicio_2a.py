from time import sleep

print('-=-'*6)
print('Login de acesso')
print('-=-'*6)

senha = int(input('Digite sua senha de acesso de 4 dígitos: '))

if senha == 1234:
    print('Processando...')
    sleep(2)
    print('Acesso com sucesso!')
else:
    print('Processando...')
    sleep(2)
    print('Senha inválida!')

