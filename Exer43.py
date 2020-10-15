"""
    algoritmo calcula o IMC
"""

peso = float(input('quantos kg voce pesa: '))
altura = float(input('qual sua altura: '))

imc = peso / (altura ** 2)  # formula do IMC

print('O IMC dessa pessoa é {:.1f}'.format(imc))

if imc < 18.5:
    print('voce esta abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('parabens voce esta na faixa de pesso normal')
elif 25 <= imc < 30:
    print('voce esta em sobrepeso')
elif 30 <= imc < 40:
    print('voce esta com obesidade')
else:
    print('voce esta com obesidade morbida')
