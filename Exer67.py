""""
    tabuada com while e for
"""

while True:
    n = int(input('informe um numero para tabuada: '))
    if n < 0:
        break
    print(f'{" Tabuada ":=^40}')
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('='*40)
print('programa encerrado')
