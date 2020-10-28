"""
    algoritmo que calcula a media de varios numeros digitados e mostra o maior e menor numero digitado
"""

resp = 'S'
maior = menor = cont = 0
media = soma = 0.0

while resp == 'S':
    num = float(input('informe um numero: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('deseja continuar [S/N]: ')).upper().strip()
media = soma / cont
print('a media de {} numeros é {}'.format(cont, media))
