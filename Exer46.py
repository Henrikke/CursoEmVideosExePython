"""
    algoritmo que faz uma contagem regresiva de 10 a 0
"""

from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('estoura fogos de artificio')
