"""
    algoritmo que acresenta um aumento no salario do funcionario
"""

salario = float(input('informe seu salario: '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('seu novo salario que era de {} agora passa a ser de {}'.format(salario, novo))
