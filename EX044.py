v = float(input('informe o valor do produto : R$'))
print('''Escolha um opção de pagamento
1 - à vista em dinheiro 10% de desconto
2 - à vista no cartão 5% de desconto
3 - em até 2x no cartão
4 - em 3x ou mais no cartão 20% de juros
''')
esc = int(input('Informe a opção desejada: '))

if esc == 1:
    final = v*0.9
    print(f'O valor fica em {final:.2f}')
elif esc == 2:
    final = v*0.95
    print(f'O valor fica em {final:.2f}')
elif esc == 3:
    print(f'O valor fica em {v}')
elif esc == 4:
    qnt = int(input('Em quantas parcelas'))
    c2 = v/qnt
    final = c2*1.2
    final2 = final*qnt
    print(f'O valor total das prestações ficara em {final2:.2f} e o valor de cada prestação fica em {final:.2f}')
else:
    print('Opção invalida')
