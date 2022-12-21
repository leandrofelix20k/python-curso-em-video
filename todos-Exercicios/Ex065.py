'''
Crie um programa que leia vários números inteiros pelo teclado. No
final da execução, mostre a média entre todos os valores e qual foi
o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores
'''

total = cont = 0
resp = 'S'

print('Insira números: ')
while resp == 'S':
    num = int(input())
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    total += num
    cont += 1
    resp = str(input('Deseja continuar[S/N]: ')).upper().strip()[0]

media = total / cont
print('\nMaior Número: {}\nMenor Número: {}\nMédia: {:.1f}'.format(maior, menor, media))
