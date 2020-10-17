"""
    detector de palindromo
"""

frase = str(input('digite a frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)

inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

if junto == inverso:
    print(f'a frase {junto} é igual a {inverso} no inverso entao e um palindromo')
else:
    print(f'a frase {junto} não é igual a {inverso} no inverso entao não e um palindromo')
