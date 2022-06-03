a = float(input('Informe a medida do primeiro lado: '))
b = float(input('Informe a medida do segundo lado: '))
c = float(input('Informe a medida do terceiro lado: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Não é possível montar um triângulo')
elif (a == b) and (a == c):
    print('Temos um triângulo equilatero')
elif (a == b) or (a == c) or (b == c):
    print('Temos um triângulo isósceles')
else:
    print('Temos um triângulo escaleno')


