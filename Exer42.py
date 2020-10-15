"""
    algoritmo verifica se os numeros passados formam uma triangulo e que tipo de triangylo forma EQUILATERO, ESCALENO, ISOSCELES
"""

r1 = float(input('informe o 1 seguimemto de reta: '))
r2 = float(input('informe o 2 seguimemto de reta: '))
r3 = float(input('informe o 3 seguimemto de reta: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('os numeros passados formam um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('os numeros passados nao formam um triagulo')
