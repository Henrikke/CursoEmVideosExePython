"""
    menu de opção para somar, subtrair, multiplicar e dividir
"""

valor1 = float(input('informe o primeiro valor: '))
valor2 = float(input('informe o segundo valor: '))

opcao = 1
while opcao != 0:
    print('''
    [1] - Somar
    [2] - Subtrair
    [3] - Multiplicar
    [4] - Dividir
    [5] - adicionar novos valores
    [0] - Sair do `Programa''')
    opcao = int(input(':'))

    if opcao == 0:
        print('programa encerrado')
    elif opcao == 1:
        print(f'A soma de {valor1} + {valor2} = {valor1 + valor2}')
    elif opcao == 2:
        print(f'A subtracao de {valor1} - {valor2} = {valor1 - valor2}')
    elif opcao == 3:
        print(f'A multiplicar de {valor1} x {valor2} = {valor1 * valor2}')
    elif opcao == 4:
        print(f'A divisao de {valor1} / {valor2} = {valor1 / valor2}')
    elif opcao == 5:
        valor1 = float(input('informe o primeiro valor: '))
        valor2 = float(input('informe o segundo valor: '))
    else:
        print(f'opcao invalida {opcao}')
