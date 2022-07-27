#Desafio 25

#Crie um programa que leia o nome de um pessoa e diga se ela tem o nome "SILVA" no nome

nome = str(input('Digite seu nome completo: '))

if(('SILVA' in nome.upper()) == True):
    print('Seu nome possui a palavra "Silva"')
else:
    print('Seu nome não possui a palavra "Silva"')
