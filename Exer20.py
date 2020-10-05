"""
    algoritmo pega quatros alunos em uma lista e embaralha em outra ordem
"""

from random import shuffle

print('{:=^60}'.format(''))

n1 = str(input('digite o 1 aluno: '))
n2 = str(input('digite o 2 aluno: '))
n3 = str(input('digite o 3 aluno: '))
n4 = str(input('digite o 4 aluno: '))

lista = [n1, n2, n3, n4]

shuffle(lista) # funcao da biblioteca random que faz uma ordem aleatoria na lista

print('{:=^60}'.format(' Alunos '))
print(lista)
print('{:=^60}'.format(''))

