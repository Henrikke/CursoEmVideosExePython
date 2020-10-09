"""
    algoritmo que calcula a velocidade e aplica uma multa se ultrapassar 80 km/h
"""

velocidade = float(input('informe a velociade atual: '))

multa = (velocidade - 80) * 7

if velocidade > 80:
    print('voce esta acima da velocidade permitida multa de {:.2f}'.format(multa))
else:
    print('velocidade segura para dirigir com segurança, tenha um bom dia ')

