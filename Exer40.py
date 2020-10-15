"""
    algoritmo que calcula a media de um aluno
"""

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

media = float((n1 + n2) / 2)

if media < 5.0:
    print(f'Media {media} aluno Reprovado')
elif 5.0 <= media <= 6.9: # elif media >= 5.0 and media <= 6.9:
    print(f'Media {media} aluno em Recuperação')
elif media >= 7.0:
    print(f'Media {media} aluno Aprovado')

