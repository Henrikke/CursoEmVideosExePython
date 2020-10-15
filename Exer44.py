"""
    algorimto que simula uma loja e calcula suas compras com descontos e ou juros
"""

print('{:=^50}'.format(' Loja '))
preco = float(input('preco das compras R$: '))
print('='*50)
print('''Informe a forma de pagamento das suas compras
[1] - pagamento a vista/cheque
[2] - a vista cartao de debito
[3] - em 2X no cartao
[4] - em 3X ou mais no cartao''')
opcao = int(input('escolha uma opcao de pagamento: '))
print('='*50)

total = preco
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    print('Sua compra sera parcelada em 2x de {:.2f}, SEM JUROS'.format(total/2))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('quantas parcelas: '))
    print('Sua compra sera parcelada em {}x de {:.2f}, COM JUROS'.format(parcelas, total/parcelas))
else:
    print('Forma de pagamento Invalida')

print('Sua compra de {:.2f} vai custar {:.2f} no final.'.format(preco, total))
print('='*50)