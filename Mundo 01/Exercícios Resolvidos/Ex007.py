#Desenvolva um programa que leia as duas notas de uma aluno, calcule e mostre sua média

nota1 = float(input('Digite a primeira nota: ')) 
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2.0

print('Sua média é igual a {:.1f}'.format(media))