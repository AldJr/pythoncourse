n = str(input('Escreva uma frase palindromo: '))
n = n.replace(" ","")
def palindromo(n):
    return n == n[::-1]
s = palindromo(n)

if s:
    print('Sim')
else:
    print('Não')