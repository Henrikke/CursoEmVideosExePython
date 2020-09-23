"""
programa que calcula o centimetro e milimetro
"""
print('{:-^40}'.format('Exercicio 7'))

metros = float(input('informe quantos metros: '))

c = metros * 100
m = metros * 1000

print('{:.2f} metros corresponde a {:.2f} centimetros'.format(metros, c))
print('{:.2f} metros corresponde a {:.2f} milimetros'.format(metros, m))

print('{:-^40}'.format(''))
