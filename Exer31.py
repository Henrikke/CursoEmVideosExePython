"""
    algoritmo que calcula quantos reais vai pagar em uma viagem
"""

distancia = float(input('informe a distancia da viagem: '))

print('tenha uma boa viagem')
valor = 0.0
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print('voce pagara {} reais na sua viagem de {} km'.format(valor, distancia))
