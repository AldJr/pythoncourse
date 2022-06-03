n = float(input('Informe sua primeira nota: '))
n1 = float(input('Informe sua segunda nota: '))

med = (n+n1)/2

if med < 5.0:
    print('Reprovado =(')
elif med >= 5.0 and med < 6.9:
    print('Recuperação =(')
else:
    print('APROVADO !')
