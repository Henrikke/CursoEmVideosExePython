"""
    algoritmo pega um numero aleatorio para voce tantar adivinhar
"""

from random import randint

comp = randint(0, 5)

print('='*50)
jogador = int(input('digite um numero para tentar adivinhar: '))

if comp == jogador:
    print('parabens voce acerto {}'.format(jogador))
else:
    print('voce erro o numero foi {} e voce escolheu {}'.format(comp, jogador))

print('='*50)