#Desafio 89

'''
Crie um programa que leia o nome e duas notas de vários alunos e 
guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
'''

dados = []
alunos = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()

    resp = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break

print('=-' * 18)
print('No.{: >5}{: >20}'.format('Nome', 'Média'))
print('--' * 16)

for i in range(0, len(alunos)):
    media = (alunos[i][1] + alunos[i][2]) / 2
    print('{}   {: <10}'.format(i+1, alunos[i][0]), end= '')
    print('{: >12}'.format(media))
    media = 0
print('--' * 16)

print('\nDigite -1 para interromper!\n')
while True:
    numAluno = int(input('Mostrar notas de qual aluno: '))
    if numAluno == -1:
        break

    print(f'Notas de {alunos[numAluno-1][0]}: {alunos[numAluno-1][1:3]}')
    print('--' * 16)
