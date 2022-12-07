#Desafio 69

'''
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Qunatas mulheres tem menos de 20 anos
'''

cont = 1
maisDezoito = 0
homens = 0
mulheresMenosVinte = 0

while True:
    print('=-' * 9)
    print(f'DADOS DA {cont}°PESSOA')
    print('=-' * 9)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo[M/F]: ')).upper()
    while sexo != 'M' and sexo != 'F':
        print('Opção Inválida')
        sexo = str(input('Digite "M" para MASCULINO e "F" para FEMININO? ')).upper()
        print(sexo)
        
    if idade > 18:
        maisDezoito += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheresMenosVinte += 1
    cont += 1

    perg = str(input('Deseja continuar[S/N]? ')).upper()
    while perg != 'S' and perg != 'N':
        print('Opção Inválida')
        perg = str(input('Digite "S" para SIM e "N" para NÃO? ')).upper()

    if perg == 'N':
        break
    
print('=-' * 14)
print(f'A- {maisDezoito} Pessoa(s) com mais de dezoito anos foram cadastradas!')
print(f'B- {homens} Homem(ns) foram cadastrados!')
print(f'C- {mulheresMenosVinte} Mulher(es) com menos de 20 anos foram cadastradas!')
print('=-' * 14)
    