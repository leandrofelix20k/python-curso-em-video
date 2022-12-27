'''
Faça um programa que nome e peso de várias pessoas, guardando em
uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves.
'''

pessoas = []
pesadas = []
leves = []

i = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))

    if i == 0:
        pesadas.append(pessoas[:])
        leves.append(pessoas[:])
    else:
        if pessoas[1] > pesadas[0][1]:
            del(pesadas)
            pesadas = []
            pesadas.append(pessoas[:])
        elif pessoas[1] == pesadas[0][1]:
            pesadas.append(pessoas[:])
        if pessoas[1] < leves[0][1]:
                del(leves)
                leves = []
                leves.append(pessoas[:])
        elif pessoas[1] == leves[0][1]:
            leves.append(pessoas[:])
    i += 1
    pessoas.clear()

    resp = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break
    
print(f'Foram cadastradas {i} pessoas!')
print(f'O maior peso foi {pesadas[0][1]}Kg. Peso de ', end= '')
for j in range(0, len(pesadas)):
    print(pesadas[j][0], end= '')
    if j < len(pesadas)-1:
        print(', ', end= '')
print(f'\nO menor peso foi {leves[0][1]}kg. Peso de ', end= '')
for k in range(0, len(leves)):
    print(leves[k][0], end= '')
    if k < len(leves)-1:
        print(', ', end= '')
print('\n')