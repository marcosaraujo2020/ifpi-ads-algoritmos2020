def main():
    numerador = denominador = 1
    somatorio = 0

    while numerador < 100:
        somatorio += numerador / denominador
        numerador += 2
        denominador += 1
    print(f'O somatório é igual {somatorio}') 

main()
