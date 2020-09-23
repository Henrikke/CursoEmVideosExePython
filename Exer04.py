"""
 programa que verifica o tipo de dado
"""

s = input('digite algo: ')

print('o tipo primitivo desse valor: ', type(s))
print('so tem espaço: ', s.isspace())
print('e um numero? ', s.isnumeric())
print('e alfabetico? ', s.isalpha())
print('e alfanumerico? ', s.isalnum())
print('esta em maiusculas? ', s.isupper())
print('esta em minuscula? ', s.islower())
print('esta capitalizada? ', s.istitle())
