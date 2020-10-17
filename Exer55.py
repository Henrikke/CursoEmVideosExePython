"""
    algoritmo calcula o maior peso e o menor peso
"""
maior = 0
menor = 0

for cont in range(1, 6):
    peso = float(input(f'informe o peso da {cont}° pessoa: '))
    if cont == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso é {maior} e o menor peso é {menor}')
