nasc = int(input('Quantos anos você tem? '))
nascm = int(input('E quantos meses? '))

if nasc < 17:
    nasc = nasc*12
    mesesv = nasc+nascm
    mesesv = 216-mesesv
    print(f'Faltam {mesesv/12:.1f} anos para você poder se alistar no exercito')
elif nasc > 18:
    nasc = nasc*12
    mesesv = nasc + nascm
    mesesf = mesesv-216
    print(f'Passou da hora do alistamento ja, ufa {mesesf/12:.1f} anos ja passaram ')
elif nasc == 18:
    print('Esta na sua hora de se alistar, boa sorte ')
