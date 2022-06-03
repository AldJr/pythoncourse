n = int(input('Informe a idade do atleta: '))
if n < 9:
    print('Mirim')
elif n < 14 and n > 9:
    print('INFANTIL')
elif 19 > n > 14:
    print('JUNIOR')
elif n < 20 and n > 19:
    print('SÊNIOR')
else:
    print('MASTER')


