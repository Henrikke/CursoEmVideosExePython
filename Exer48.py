"""
    algoritmo que calcula os numeros impare e multiplos de 3
"""

soma = 0
cont = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1
        soma += n

print(f'a quantidade de numeros impares é {cont} e a soma é {soma}')
