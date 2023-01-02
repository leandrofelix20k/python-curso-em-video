'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média
'''

pessoa = {}
pessoasCadastradas = []

i = 1
while True:
    print('{:-^33}'.format(f'Dados da Pessoas N°{i}'))
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
            pessoa['sexo'] = str(input('ERRO! Digite apenas M ou F: ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    pessoasCadastradas.append(pessoa.copy())
    pessoa.clear()

    perg = str(input('Deseja continuar[S/N]: ')).upper().strip()[0]
    while perg not in 'SN':
            perg = str(input('ERRO! Digite apenas S ou N: ')).upper().strip()[0]
    if perg == 'N':
        break
    i += 1

soma = 0
for j in range(0, len(pessoasCadastradas)):
    soma = soma + pessoasCadastradas[j]['idade']
media = soma / i

print('=-'* 15)
print(f'-O grupo tem {i} pessoas.')
print(f'-A média de idade é de {media:.2f} anos.')
print('-As mulheres cadastradas foram: ', end= '')
for j in range(0, len(pessoasCadastradas)):
    if pessoasCadastradas[j]['sexo'] == 'F':
        print(f'{pessoasCadastradas[j]["nome"]}', end= '')
        if j < len(pessoasCadastradas) - 1:
            print(', ', end='')
        else:
            print('.')

print('-Lista de pessoas que estão acima da média de idade: \n')
for j in range(0, len(pessoasCadastradas)):
    if pessoasCadastradas[j]['idade'] > media:
        for k, v in pessoasCadastradas[j].items():
            print(f'{k} = {v};', end= ' ')
    print()
