import random
aluno1 = str(input('Escolha o nome do primeiro aluno : '))
aluno2 = str(input('Escolha o nome do segundo aluno : '))
aluno3 = str(input('Escolha o nome do terceiro aluno : '))
aluno4 = str(input('Escolha o nome do quarto aluno : '))
list = (aluno1, aluno2, aluno3, aluno4)
sorteio = random.sample(list)
print(f'O aluno ganhador foi {sorteio}')
