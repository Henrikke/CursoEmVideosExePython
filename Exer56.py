"""
    algoritmo que pega um numero de pessoas e verifica qual e o homen mais velho e a mulher com menos de 20 anos de idade
"""

mediaIdade = 0.0
mulherMenor = 0
homemVelho = ''
idadeHomen = 0

for cont in range(1, 5):
    print('-'*60)
    print('{}° {}'.format(cont, ' Pessoa '))
    nome = str(input('nome da pessoa: '))
    idade = int(input('idade da pessoa: '))
    sexo = str(input('sexo [M = Masculino] [F = Feminino]: '))
    mediaIdade += idade

    if cont == 1 and sexo in 'Mm':
        idadeHomen = idade
        homemVelho = nome

    if idade > idadeHomen and sexo in 'Mm':
        idadeHomen = idade
        homemVelho = nome

    if idade < 20 and sexo in 'Ff':
        mulherMenor += 1
print('-'*60)
print(f'A media da idade do grupo é {mediaIdade/4}')
print(f'O homem mais velho tem {idadeHomen} anos e se chama {homemVelho}')
print(f'no grupo tem {mulherMenor} que tem menos de 20 anos de idade')
print('-'*60)
