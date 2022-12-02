 #Desafio 65

 #Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

maior = 0
menor = 0
total = 0
cont = 0
resp = 'S'

print('Insira números: ')
while resp == 'S':
    num = int(input())
    if cont == 0:
        maior = num
        menor = num
        total = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        total = total + num
    cont += 1
    resp = str(input('Deseja continuar[S/N]: ').upper())

media = total / cont
print('\nMaior Número: {}\nMenor Número: {}\nMédia: {}'.format(maior, menor, media))