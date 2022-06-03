print('*'*10,'Escolha em qual medida a temperatura será medida!!!','*'*10)
print('')
print('')
print('1- Celsius para farenheit')
print('2- Farenheit para celsius')
o = float(input('qual opção desejada ? '))
if o == 1:
 cel = int(input('Insira o valor em celsius :'))
 cal = (cel*9/5)+32
 print('Sua temperatura em Farenheit é {}'.format(cal))
else :
 farheit = int(input('Insira o valor em Farenheit'))
 calcc = (farheit-32)*5/9
 print('Sua temperatura em celsius é {}'.format(calcc))