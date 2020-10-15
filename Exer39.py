"""
    algoritmo que calcula o ano do seu alistamento do quartel
"""

from datetime import date

atual = date.today().year
nasc = int(input('informe o ano do seu nascimento: '))
idade = atual - nasc

print('quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('voce precisa fazer seu alistamento imediatamente')
elif idade < 18:
    anos = 18 - idade
    tempo = atual + anos
    print('ainda falta {} anos para o alistamento'.format(anos))
    print('seu alistamento sera em {} ano'.format(tempo))
elif idade > 18:
    anos = idade - 18
    tempo = atual - anos
    print('voce ja deveria ter se alistado em {} anos'.format(anos))
    print('seu alistamento foi em {}'.format(tempo))

