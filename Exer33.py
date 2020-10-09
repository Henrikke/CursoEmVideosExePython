"""
    algoritmo pega 3 numeros e mostra qual e o maior deles
"""

n1 = int(input('informe o 1 numero: '))
n2 = int(input('informe o 2 numero: '))
n3 = int(input('informe o 3 numero: '))

if n1 > n2 and n1 > n3:
    print('o numero maior e {} n1'.format(n1))
if n2 > n1 and n2 > n3:
    print('o numero maior e {} n2'.format(n2))
if n3 > n1 and n3 > n2:
    print('o numero maior e {} n3'.format(n3))
