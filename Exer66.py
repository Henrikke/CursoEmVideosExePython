""""
    algoritmo que soma varios numeros ate voce parar o pragrama
"""

soma = 0
cont = 0

while True:
    numero = int(input('informe um numero ou digite 999 para sair: '))

    if numero == 999:
        break
    soma += numero
    cont += 1

print(f'a quantidade de numeros digitados foi {cont} e a soma é {soma}')
