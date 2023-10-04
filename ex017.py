'''from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = sqrt((co ** 2)+(ca ** 2))
print('A hipotenusa vai medir {:.2f}'.format(hip))'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))
