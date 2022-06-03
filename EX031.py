n = int(input('Qual a distância da sua viagem em Km ? '))
if n <= 200:
    n = n*0.5
    print(f'O valor gasto total é {n:.2f}R$')
else:
    n = n*0.45
    print(f'O valor gasto total é {n:.2f}R$')
