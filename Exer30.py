"""
    algoritmo que verifica se um numero e par ou impar
"""

numero = int(input('informe um numero gualquer: '))

resultado = numero % 2

if resultado == 1:
    print('o numero informado {} e impar'.format(numero))
else:
    print('o numero informado {} e par'.format(numero))
