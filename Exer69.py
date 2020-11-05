"""
    algoritmo que pega a idade e sexo de varias pessoas e filtra por idade e sexo
"""
total18 = totalHomen = totalMulher20 = 0

print(f'\033[31m{" Cadastro ":=^45}\033[m')
while True:

    idade = int(input('informe sua idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('informe seu sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        total18 += 1

    if sexo == 'M':
        totalHomen += 1

    if idade < 20 and sexo == 'F':
        totalMulher20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('deseja continuar [S/N]: ')).strip().upper()[0]

    if resp == 'N':
        break
    print('\033[31m=\033[m' * 45)
print('\033[31m=\033[m'*45)

print(f'o total de pessoas com 18 ou mais anos {total18}')
print(f'total de homens cadastrados {totalHomen}')
print(f'total de mulheres com menos de 20 anos {totalMulher20}')

print('\033[31m=\033[m'*45)