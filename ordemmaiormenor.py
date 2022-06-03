cores = {
         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'branco':'\033[30m',
         'roxo':'\033[35m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'limpa':'\033[m',
         'pretoebranco':'\033[7;30;m'
}

n = int(input('Me fale o primeiro numero: '))
n2 = int(input('Me fale o segundo numero: '))
n3 = int(input('Me fale o terceiro numero: '))
numbers = [n, n2, n3]
numbers.sort(reverse=True)

print('ordem do maior para o menor\033[35m', numbers)
