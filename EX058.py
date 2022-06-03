import random
vezes = 1
numero = random.randint(0,10)
adv = int(input('Qual seu chute? '))
while adv != numero:
    numero = random.randint(0, 10)
    adv = int(input('Qual seu chute? '))
    vezes += 1
print('Parabêns você ganhou !!')
print(f'Você precisou de {vezes} vezes para ganhar')


