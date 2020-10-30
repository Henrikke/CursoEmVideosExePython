"""
    jogo par ou impar
"""

from random import randint
v = 0
while True:
    jogador = int(input('informe um valor: '))
    computador = randint(0, 10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('par ou impar [P/I]: ')).strip().upper()[0]
        print(f'a jogada do computador foi {computador} e a sua jogada foi {jogador}')
        print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('deu PAR voce ganhou')
            v += 1
        else:
            print('deu IMPAR voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('deu IMPAR voce ganhou')
            v += 1
        else:
            print('deu PAR voce perdeu')
            break
    print('vamos jogar novamente')

print(f'voce ganhou {v} vezes')