"""
    mostra o primeiro nome e o ultimo sobrenome
"""

nome = str(input('informe seu nome completo: ')).strip()

n = nome.split()
q = int(len(nome)-1)

print('seu primeiro nome é: ', n[0])



