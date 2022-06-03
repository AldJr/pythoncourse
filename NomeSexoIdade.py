nomeHomem = ''
idades = 0
velho = 0
fem = 0
for c in range(0, 4):
    nome = str(input(f'Qual o nome do individuo {c}: '))
    idade = int(input(f'Qual a idade do individuo {c}: '))
    sexo = str(input(f'Qual o sexo do individuo {c} M/F : '))
    if sexo == 'M':
        if idade > velho:
            velho = idade
            nomeHomem = nome
    if sexo == 'F':
        if idade < 20:
            fem += 1
    idade += idade
print(f'O individuo mais velho masculino é o{nomeHomem} e tem {velho}')
print(f'A média de idade deste grupo é {idade/4}')
print(f'Nesse grupo existem {fem} mulheres com idade abaixo de 20 anos')

