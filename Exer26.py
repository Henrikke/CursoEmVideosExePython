"""
    verifica quantas ocorrencias de a uma frase teve
"""

frase = str(input('informe um frase: ').upper().strip())

print('a letra A teve: {} ocorrencias na frase'.format(frase.count('A')))
print('a primeira ocorrencia de A na frase foi na posição: ', frase.find('A')+1)
print('A ultima ocorrencia de A foi na posição: ', frase.rfind('A'))
