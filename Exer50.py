"""
    algorimto que soma os numeros pares e contam quantos numeros pares
"""

soma = 0
cont = 0

for c in range(1, 7):
    n = int(input(f'informe {c}° valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'a quantidade de numeros pares é {cont} e a soma {soma}')
