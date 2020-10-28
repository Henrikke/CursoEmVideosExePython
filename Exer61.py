"""
    progresao aritmetica editada
"""
primeiro = int(input('primeiro termo: '))
razao = int(input('razao da pa: '))

termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f' {termo} -> ', end='')
        cont += 1
        termo += razao
    mais = int(input('\nquantos termos vai querer mais ou digite 0 para cancelar: '))
print('fim da pa')
