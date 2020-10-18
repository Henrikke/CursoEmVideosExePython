"""
    valida o sexo de uma pessoa m para masculino ou f para feminino
"""

sexo = str(input('informe o sexo da pessoa M/F: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('informe o sexo da pessoa M/F: ')).strip().upper()[0]

print(f'O sexo {sexo} registrado com sucesso')
