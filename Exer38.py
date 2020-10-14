"""
    algoritmo que verifica qual numero e maior
"""

print('{:-^50}'.format(' Compara qual numero maior '))
n1 = int(input('informe o primeiro numero: '))
n2 = int(input('informe o segundo numero: '))

print('-'*50)
if n1 > n2:
    print('o primeiro numero {} maior que {}'.format(n1, n2))
elif n2 > n1:
    print('o segundo numero {} maior que {}'.format(n2, n1))
else:
    print('numero {} igual {}'.format(n1, n2))
print('-'*50)
