v1 = float(input('Qual sua velocidade ?'))
multa = (v1-80)*7
if v1 <= 80:
    print('Você esta dentro da velocidade estabelecida.')
else:
    print(f'\033[35mVocê ultrapassou o limite de velocidade sua multa foi\033[30m {multa:.0f}R$')

