"""
    algoritmo mostra se um numero e primo ou nao
"""

numero = int(input('informe um numero: '))
cont = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')
        cont += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO numero {numero} foi divisivel por {cont}')
if cont == 2:
    print('O Numero é PRIMO')
else:
    print('O Numero não é PRIMO')
