"""
    algoritmo que simula um mercado e filtra o maior valor e o menor preco dos produtos
"""
print('-'*60)
print(f'\033[36m{" LOJA KI-BARATO ": ^60}\033[m')
print('-'*60)

nomePrecoMenor = ''
precoMenor = preco = precoTotal = 0.0
cont = precoMil = 0

while True:
    produto = str(input('informe o nome do produto: '))
    preco = float(input('informe o preco do produto R$:'))
    cont += 1
    precoTotal += preco

    if preco > 1000:
        precoMil += 1

    if preco < precoMenor or cont == 1:
        precoMenor = preco
        nomePrecoMenor = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('deseja continuar? [S/N]: ')).strip().upper()[0]

    if resp == 'N':
        break
    print('-' * 60)

print('-'*60)
print(f'\033[36m{" Total da Compra ": ^60}\033[m')
print('-'*60)
print(f'o total da compra deu R$:{precoTotal:.2f}')
print(f'a quantidade de produtos de mais de mil reais é {precoMil}')
print(f'o produto {nomePrecoMenor} custa {precoMenor: .2f} é o mais barato')
print('-'*60)
