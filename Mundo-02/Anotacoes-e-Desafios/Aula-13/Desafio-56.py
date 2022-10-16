#Desafio 56

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres tem mais de 20 anos.

print('Digite, a seguir, o nome, idade e o sexo de 4 pessoas: ')
print('Para o sexo, digite M ou F!\n')

mediaIdade = 0
idadeMaisVelho = 0
mulheresMenosVinte = 0
cont = 0
for i in range(0,4):
    nome = str(input('Nome pessoa N°{}: '.format(i+1)))
    idade = int(input('Idade pessoa N°{}: '.format(i+1)))
    sexo = str(input('Sexo pessoa N°{}: '.format(i+1))).upper()
    print('-=' * 10)

    mediaIdade += idade / 4

    if(sexo == 'M' and idadeMaisVelho > idade):
        nomeMaisVelho = nome
        cont += 1
    
    if(sexo == 'F' and idade < 20):
        mulheresMenosVinte += 1

print('\nA média de idade do grupo é: {:.0f} Anos'.format(mediaIdade))
if(cont > 0):
    print('O senhor mais velho é: {}'.format(nomeMaisVelho))
else:
    print('Não consta nenhuma pessoa do sexo masculino nessa lista')
print('Do grupo, {} mulheres tem menos de 20 anos'.format(mulheresMenosVinte))
