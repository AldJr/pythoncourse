n = int(input('Informe seu salario que informaremos seu aumento: '))
if n > 1250:
    n = n*1.1
    print(f'seu novo salario sera {n:.0f}R$!')
else:
    n = n*1.15
    print(f'seu novo salario sera {n:.0f}R$!')
