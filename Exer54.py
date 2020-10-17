"""
    categoria de idade maior de idade ou menor de idade
"""

from datetime import date

atual = date.today().year

maior = 0
menor = 0

print(f'{ " Categoria de Idade ":=^60}')
for i in range(1, 7):

    nasc = int(input(f'qual é o ano do nascimeto da {i}° pessoa: '))
    idade = atual - nasc

    if idade >= 21:
        maior += 1
        print(f'\033[31mMAIOR[{idade}]\033[m')
    else:
        menor += 1
        print(f'\033[32mMENOR[{idade}]\033[m')
print('='*60)
print(f'a quantidade de pessoas com maior idade é {maior}')
print(f'a quantidade de pessoas com menor idade é {menor}')
print('='*60)
