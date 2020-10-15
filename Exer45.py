"""
    algoritmo que simula o jogo de jokenpo com a maquina
"""

from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')

computador = randint(0, 2)

print(f'{" JOKENPO ":=^50}')
print('''Escolha sua Jogada
[0] - Pedra 
[1] - Papel
[2] - Tesoura''')
jogador = int(input('Escolha uma opacao: '))
print('='*50)

if jogador > 2:
    print(f'\033[31mJogada Invalida \033[m')

if computador == 0:  #Pedra
    if jogador == 0: #Pedra
        print('houve empate')
    elif jogador == 1:  #Papel
        print('Papel ganha de Pedra: Jogador venceu')
    elif jogador == 2:  #Tesoura
        print('Pedra ganha de Tesoura: Computador venceu')
elif computador == 1:  #Papel
    if jogador == 0:  #Pedra
        print('Papel ganha de pedra: Computador venceu')
    elif jogador == 1:  #Papel
        print('houve empate')
    elif jogador == 2:  #Tesoura
        print('Tesoura ganha de Papel: Jogador venceu')
elif computador == 2:  #Tesoura
    if jogador == 0:  #Pedra
        print('Pedra ganha de Tesoura: Jogador venceu')
    elif jogador == 1:  #Papel
        print('Tesoura ganha de Papel: Computador venceu')
    elif jogador == 2:  #Tesoura
        print('houve empate')

print('='*50)
