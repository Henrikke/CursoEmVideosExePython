"""
    algoritmo que calcula a soma de varios numeros
"""

cont = soma = numero = 0

numero = int(input('informe o numero e [999] para parar: '))

while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('informe o numero e [999] para parar: '))

print('a soma de {} foi {}'.format(cont, soma))
