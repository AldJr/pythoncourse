soma = 0
for c in range(4, 11):
    if c %2 == 0:
        soma += c
        if soma %2 != 0:
            quit()
        print(soma)
