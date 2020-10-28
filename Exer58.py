"""
    algoritmo que calcula se voce acerto o palpite do computador(jogo da advinhação)
"""

from random import randint

computador = randint(0, 10)
acerto = False
palpites = 0
jogador = 0

while not acerto:
    jogador = int(input('digite seu palpite para acerta a jogada do computador: '))
    palpites += 1
    if computador == jogador:
        acerto = True
    else:
        if jogador > computador:
            print('menos... tente outra vez')
        elif jogador < computador:
            print('mais... tente outra vez')
print(f'parabens vo acerto com {palpites} tentativas o palpite foi {jogador}')
