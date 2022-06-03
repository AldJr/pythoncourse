n = int(input('Digite um ano para saber se ele é bissexto: '))
if n%4 == 0:
    print('Este ano é bissexto')
elif n%1000 == 0:
    print('Esse ano é bissexto')
else:
    print('este ano não é bissexto')