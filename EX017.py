import math
x = int(input('Informe o cateto oposto : '))
y = int(input('informe o cateto adjacente : '))
x1 = (x**2)+y**2
hipotenusa = math.sqrt(x1)

print('O valor da hipotenusa deste triangulo é {}'.format(hipotenusa))

