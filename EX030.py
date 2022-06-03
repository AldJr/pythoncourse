n = int(input('Digite um numero para saber se é impar ou par: '))
if n%2 == 0:
    print('\033[1;34;40mEste número é par\033[m')
else:
    print('\033[1;35;107meste número é impar\033[m')