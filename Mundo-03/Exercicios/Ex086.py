'''
Crie um programa que crie uma matriz 3x3 e preencha com valores  
lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta.
'''

matriz = [[], [], []]

print('Digite nove números: ')
for i in range(0, 9):
    if i < 3:
        matriz[0].append(int(input()))
    elif i < 6:
        matriz[1].append(int(input()))
    else:
        matriz[2].append(int(input()))

print('{:-^20}'.format('Matriz 3x3'))

