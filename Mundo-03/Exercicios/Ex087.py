'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitado.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[], [], []]
somaPares = somaTerceiraColuna = maiorNumSegundaLinha = 0

print('Digite nove números: ')
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input('Digite um valor para [{}, {}]: '.format(l, c))))

print('\n')
print('{:-^20}'.format('Matriz 3x3'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end= '')
        if matriz[l][c] % 2 == 0:
            somaPares = somaPares + matriz[l][c]
        if c == 2:
            somaTerceiraColuna = somaTerceiraColuna + matriz[l][c]
        if l == 1:
            if c == 0: 
                maiorNumSegundaLinha = matriz[l][c]
            else:
                if matriz[l][c] > maiorNumSegundaLinha:
                    maiorNumSegundaLinha = matriz[l][c]
    print('\n')
print('-' * 20)

print(f'A soma dos números pares foi: {somaPares}')
print(f'A soma dos números da terceira coluna foi: {somaTerceiraColuna}')
print(f'O maior número na segunda linha é {maiorNumSegundaLinha}')
