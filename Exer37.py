"""
    algoritmo que faz a conversao de decimal para binario octal ou hexadecimal
"""

print('='*60)
numero = int(input('informe um numero em decimal para a conversao: '))

print('''Escolha uma das opçoes para fazer a conversao
[1] - conversao para binario
[2] - conversao para octal
[3] - conversao para hexadecimal''')

opcao = int(input('informe a opacao: '))
print('='*60)

if opcao == 1:
    print('A conversao de {} para binario é \033[32m{}\033[m'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('A conversao de {} para octal é \033[32m{}\033[m'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('A conversao de {} para hexadecimal é \033[32m{}\033[m'.format(numero, hex(numero)[2:]))
else:
    print('\033[31mOpcao Invalida\033[m')

print('='*60)
