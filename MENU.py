n = int(input('Digite seu primeiro numero :'))
n2 = int(input('Digite seu segundo numero :'))
print('-'*20,'MENU','-'*20)
print('''Escolha uma das operações a realizar com os numeros que voce nos mandou
[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS NÚMEROS
[5] - SAIR DO PROGRAMA
''')
c = int(input('Digite sua operação :'))
while c != 5:
    while c == 1:
       print(n+n2)
       print('''Escolha uma das operações a realizar com os numeros que voce nos mandou
       [1] - SOMAR
       [2] - MULTIPLICAR
       [3] - MAIOR
       [4] - NOVOS NÚMEROS
       [5] - SAIR DO PROGRAMA
       ''')
       c = int(input('O gostaria de fazer em seguida? '))
    while c == 2:
        print(n*n2)
        print('''Escolha uma das operações a realizar com os numeros que voce nos mandou
               [1] - SOMAR
               [2] - MULTIPLICAR
               [3] - MAIOR
               [4] - NOVOS NÚMEROS
               [5] - SAIR DO PROGRAMA
               ''')
        c = int(input('O que gostaria de fazer em seguida ?'))
    while c == 3:
        if n > n2:
            print(f'O maior numero é {n}')
            print('''Escolha uma das operações a realizar com os numeros que voce nos mandou
                           [1] - SOMAR
                           [2] - MULTIPLICAR
                           [3] - MAIOR
                           [4] - NOVOS NÚMEROS
                           [5] - SAIR DO PROGRAMA
                           ''')
            c = int(input('O que gostaria de fazer em seguida ?'))
        elif n == n2:
            print('Os dois valores são iguais')
            print('''Escolha uma das operações a realizar com os numeros que voce nos mandou
                           [1] - SOMAR
                           [2] - MULTIPLICAR
                           [3] - MAIOR
                           [4] - NOVOS NÚMEROS
                           [5] - SAIR DO PROGRAMA
                           ''')
            c = int(input('O que gostaria de fazer em seguida ?'))
        else:
            print(f'O maior numero é {n2}')
            print('''Escolha uma das operações a realizar com os numeros que voce nos mandou
               [1] - SOMAR
               [2] - MULTIPLICAR
               [3] - MAIOR
               [4] - NOVOS NÚMEROS
               [5] - SAIR DO PROGRAMA
               ''')
            c = int(input('O que gostaria de fazer em seguida ?'))
    while c == 4:
        n = int(input('Digite seu primeiro numero :'))
        n2 = int(input('Digite seu segundo numero :'))
        c = int(input('O gostaria de fazer em seguida? '))


print('Até a proxima =)')