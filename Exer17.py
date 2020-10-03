"""
    faz o calculo da hipotenusa
"""
from builtins import print
from math import hypot

ca = float(input('informe o cateto adjacente: '))
co = float(input('informe o cateto oposto: '))

hi = hypot(co, ca)

print('o calculo da hipotenusa é: {:.2f}'.format(hi))
