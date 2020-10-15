"""
    algoritmo que calcula a categoria de um atleta pela sua idade
"""

from datetime import date

nasc = int(input('informe o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JUNIOR')
elif idade <= 25:
    print('Atleta SENIOR')
elif idade > 25:
    print('Atleta MASTER')
