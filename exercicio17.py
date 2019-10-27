''''co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medi {:.2f}'.format(hip))'''

'''import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hip = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))'''

from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))