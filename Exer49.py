"""
    tabuada usando o for
"""
print('='*30)
tabuada = int(input('informe a tabuada: '))
print(f'{" Tabuada ":=^30}')
for n in range(1, 11):
    print(f'{tabuada} X {n} = {tabuada * n}')
print('='*30)
