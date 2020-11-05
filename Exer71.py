"""
    simula um banco e fala quantos cedulas voce recebera pela quantia do valor informado
"""

print('='*60)
print(f'{" BANCO ":^60}')
print('='*60)

valor = int(input('informe o valor a ser sacado: '))
ced = 50
totalCed = 0
total = valor

while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'total de {totalCed} cedulas de {ced} reais')

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0

        if total == 0:
            break
print('='*60)
