n = float(input('Informe sua altura EX: 1.80 '))
m = float(input('Informe seu peso em kg:'))

imc = m/(n*n)

if imc < 18.5:
    print('Você esta abaixo do peso')
elif 25 > imc > 18.5:
    print('Peso ideal')
elif 30 > imc > 25:
    print('Sobrepeso')
elif 40 > imc > 30:
    print('Obesidade')
else:
    print('Obesidade mórbida')

