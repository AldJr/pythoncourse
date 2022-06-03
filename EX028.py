import random

numero = random.randint(0,6)
adv = int(input('Qual seu chute? '))
if numero == adv:
    print('Acertou meus parabêns!!')
else:
    print('Infelizmente não foi desta vez =(')

