pt = int(input('Escreva o primeiro termo da PA: '))
razao = int(input('Escreva a razão desta PA: '))
an = pt + (10 - 1)*razao
for c in range(pt, 125, razao):
    print(c)
