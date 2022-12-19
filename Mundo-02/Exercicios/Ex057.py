'''
Faça um programa que leia o sexo de uma pessoas, mas só aceite os 
valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente 
até ter um valor correto
'''

sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    print(sexo)
    sexo = str(input('Digite apenas M ou F: '))

print(f'Sexo {sexo} foi registrado!')
