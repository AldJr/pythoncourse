n = int(input('Qual o valor da casa que quer comprar? '))
s = int(input('Qual seu salario? '))
a = int(input('Em quantos anos você gostaria de pagar? '))
# vendo a quantidade necessaria por mes em x anos para pagar a casa, sem ultrapassar os 30%
soma = (n/a)/12
# salario em 30%
soma2 = s*0.3
if soma > soma2 :
    print('Não foi possivel fazer seu empréstimo =(')
else:
    print('seu emprestimo foi aprovado =)')
