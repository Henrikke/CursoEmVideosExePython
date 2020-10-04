"""
    faz uma escolha entre alunos de uma lista usando a funcao choice de random
"""

from random import random, choice

n1 = input('informe o primeiro aluno: ')
n2 = input('informe o segundo aluno: ')
n3 = input('informe o terceiro aluno: ')
n4 = input('informe o quarto aluno: ')

lista = (n1, n2, n3, n4)
escolhido = choice(lista)

print('o escolhido foi: {}'.format(escolhido))
