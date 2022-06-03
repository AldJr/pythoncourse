pesado = 0
leve = 0
for c in range(1, 10):
    peso = float(input('Digite o peso da {}ª pessoa:'.format(c)))
    if c == 1:
        pesado = peso
        leve = peso
    if peso > pesado:
        pesado = peso
    if peso < leve:
        leve = peso
print('O mais leve pesa {:.2f}kg'.format(leve))
print('O mais pesado pesa {:.2f}kg'.format(pesado))