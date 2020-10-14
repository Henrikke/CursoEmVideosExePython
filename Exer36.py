"""
    algoritmo que calcula se um emprestimo pode ser aprovado para comprar uma casa
"""

casa = float(input('informe o valor da casa: '))
salario = float(input('digite seu salario quantos voce ganha por mes: '))
anos = int(input('informe em quantos anos voce deseja pagar: '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de {:.2f} em {} anos a prestaçao sera de {:.2f}'.format(casa, anos, prestacao))

if prestacao <= minimo:
    print('\033[36memprestimo concedido\033[m')
else:
    print('\033[31memprestimo negado\033[m')

