import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {:.0f} tem o SENO de {:.1f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {:.0f} tem o COSSENO de {:.1f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {:.0f} tem a TANGENTE de {:.1f}'.format(angulo, tangente))


