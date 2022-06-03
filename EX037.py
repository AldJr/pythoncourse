n = int(input('Digite um numero: '))
print('''Escolha a opção da conversão
1 - Numero para binario\n
2 - Numero para octal\n
3 - Numero para hexadecimal''')
c = int(input('Escolha uma opção: '))

if c == 1:
    print(bin(n))
elif c == 2:
    print(oct(n))
elif c == 3:
    print(hex(n))
else:
    print('Escolha um opção valida de 1 a 3 =)')