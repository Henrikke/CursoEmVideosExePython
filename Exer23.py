"""
    calculando um algoritmo que mostra a unidade dezena centena e milhar
"""

print('{:-^60}'.format(''))
numero = int(input('digite um numero: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('{:-^60}'.format(''))

print('a unidade do numero informado e: ', u)
print('a dezena do numero informado e: ', d)
print('a centena do numero informado e: ', c)
print('a miliar do numero informado e: ', m)

print('{:-^60}'.format(''))
