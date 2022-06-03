from time import sleep
import random

print('''Escolha uma opção para o jogo de jokenpô
1 - Pedra
2 - Papel
3 - Tesoura
''')
esc = int(input('Escolha : '))

escbot = random.randint(1, 3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

if esc == 1 and escbot == 1:
    print('EMPATE, vocês dois escolheram pedra')
elif esc == 1 and escbot == 2:
    print('A NÃO o robo ganhou de você com o papel')
elif esc == 1 and escbot == 3:
    print('MEUS PARABÉNS VOCÊ GANHOU')
elif esc == 2 and escbot == 1:
    print('MEUS PARABÉNS VOCÊ GANHOU')
elif esc == 2 and escbot == 2:
    print('EMPATE, vocês dois escolheram papel')
elif esc == 2 and escbot == 3:
    print('A NÃO o robo ganhou de você com a tesoura')
elif esc == 3 and escbot == 1:
    print('A NÃO o robo ganhou de você com pedra')
elif esc == 3 and escbot == 2:
    print('MEUS PARABÉNS VOCÊ GANHOU')
elif esc == 3 and escbot == 3:
    print('EMPATE, vocês dois escolheram tesoura')
else:
    print('Escolha uma opção valida')
    quit()