"""
    algoritmo que mostra se no começo de uma frase tem meu nome
"""

frase = str(input('informe a frase: ')).strip()

print(frase[:8].upper() == 'HENRIQUE')
