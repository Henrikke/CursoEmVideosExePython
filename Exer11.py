"""

 calcula a area de uma parede e quantos de tinta precisara para pintar a parede
"""

largura = float(input('qual a largura da parede: '))
altura = float(input('qual a altura da parede: '))

area = largura * altura

print('a parede tem uma area de {}m^2'.format(area))

tinta = area / 2

print('voce precisara de {} litros de tinta para pintar a parede'.format(tinta))
