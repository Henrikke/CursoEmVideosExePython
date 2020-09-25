"""

 programa que concede 5 % de desconto em produtos
"""

valor = float(input('quanto vale o produto: '))

desconto = valor * 0.05

print('o produto vale {} aplicando 5% de desconto ele cai para {} '.format(valor,(valor - desconto)))
