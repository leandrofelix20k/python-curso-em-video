#Desafio 57

#Faça um programa que leia o sexo de uma pessoas, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input('Digite seu sexo[M/F]: '))

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite apenas M ou F: ')).upper()
