#Desafio 90

'''
Faça um programa que leia nome e média de um aluno. Guardando em um
dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

print('-='*13)
print(f'Nome do aluno: {aluno["nome"]}')
print(f'A média dele foi {aluno["media"]:.1f}')

if aluno['media']  >= 7.0:
    print('O discente foi: APROVADO!')
else:
    print('O discente foi: REPROVADO!')
print('-='*13)
