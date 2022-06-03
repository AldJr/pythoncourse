import math

x = int(input('Informe o valor do angulo a ser calculado : '))
x1 = math.radians(x)
y = math.cos(x1)
y1 = math.sin(x1)
y2 = math.tan(x1)
print('O valor do angulo {} graus em cosseno é {} em seno é {} e em tangente é {} '.format(x, y, y1, y2))
