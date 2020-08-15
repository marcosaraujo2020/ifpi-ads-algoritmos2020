from time import sleep
def eval_loop():
    while True:
        termo = str(input('Digite uma expressão matemática ou digite "done" para SAIR ')).lower()
        if termo == 'done':
            print('Encerrando.....')
            sleep(2)
            break
        print(eval(termo))
eval_loop()
