"""
    faz o calculo de seno coseno e tangente
"""

from math import radians, sin, cos, tan

print('{:-^60}'.format(' Calculo Trigonometrico '))
angulo = float(input('digite um angulo desejado: '))

#faz a conversao para radianos
radiano = radians(angulo)

print('o seno do angulo {:.2f} é: {:.2f}'.format(angulo, sin(radiano)))
print('o coseno do angulo {:.2f} é: {:.2f}'.format(angulo, cos(radiano)))
print('a tangente do angulo {:.2f} é: {:.2f}'.format(angulo, tan(radiano)))

print('{:-^60}'.format(''))
