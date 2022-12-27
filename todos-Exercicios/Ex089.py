#Desafio 89

'''
Crie um programa que leia o nome e duas notas de vários ficha e 
guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
'''

dados = []
ficha = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    ficha.append(dados[:])
    dados.clear()

    resp = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break

print('=-' * 18)
print('No.{: >5}{: >20}'.format('Nome', 'Média'))
print('--' * 16)

for i in range(0, len(ficha)):
    media = (ficha[i][1] + ficha[i][2]) / 2
    print('{}   {: <10}'.format(i+1, ficha[i][0]), end= '')
    print('{: >12.1f}'.format(media))
    media = 0
print('--' * 16)

print('\nDigite -1 para interromper!\n')
while True:
    numAluno = int(input('Mostrar notas de qual aluno: '))
    if numAluno == -1:
        break

    print(f'Notas de {ficha[numAluno-1][0]}: {ficha[numAluno-1][1:3]}')
    print('--' * 16)
