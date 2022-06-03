for c in range(1, 8):
    a = int(input('Qual o ano de nascimento ? '))
    if 2022 > a > 2004:
        print('esta é menor')
    elif a > 2022:
        print('Ano invalido')
    else:
        print('essa é maior')

