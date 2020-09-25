"""
 calcula aumento do funcionario
"""

salario = float(input('quanto e o salario do funcionario: '))

aumento = salario * (15 / 100)

print('o salario que era de {} com o aumento de 15% fica {}'.format(salario,aumento+salario))
