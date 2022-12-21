#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
print('Digite o ano de nascimento de 7 pessoas: ')
anoAtual = date.today().year

numMaiores = 0
numMenores = 0
for i in range(0, 7):
    anoNascimento = int(input('Ano de nascimento da pessoa N°{}: '.format(i+1)))
    idade = anoAtual - anoNascimento

    if(idade >= 21):
        numMaiores +=1
    else:
        numMenores +=1

print('\nNúmero de pessoas com mais de 18 anos: {}'.format(numMaiores))
print('Número de pessoas com idade inferior a 18 anos: {}'.format(numMenores))
