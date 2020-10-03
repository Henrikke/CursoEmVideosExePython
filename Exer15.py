"""
    calcula o aluguel de um carro, a cada dia paga 60 reais e 0,15 por km rodado
"""

dia = int(input('quantos dias passo com o carro? '))
km = float(input('quantos km rodado com o carro? '))

print('total a pagar é: {:.2f}'.format((dia * 60)+(km * 0.15)))
