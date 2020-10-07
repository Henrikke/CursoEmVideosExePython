"""
    algoritmo que mostra uma frase em letras maiusculas minusculas e a quantidade de letras
"""

print('{:-^60}'.format(''))
frase = str(input('digite seu nome: '))

print('seu nome em maiusculo: ', frase.upper())
print('seu nome em minusculo: ', frase.lower())
print('seu nome tem: ', len(frase.strip()))

print('{:-^60}'.format(''))
