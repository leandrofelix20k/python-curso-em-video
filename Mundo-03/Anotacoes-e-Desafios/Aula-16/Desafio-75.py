#Desafio 75

'''
Desenvolva um programa que leia valores pelo teclado e guarde-os em 
uma tupla. No final, mostre:

A)Quantas vezes apareceu o valor 9.

B)Em que posição foi digitado o primeiro valor.

C)Quais foram os números pares.
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite outro número: '))
tupla = (n1, n2, n3, n4)


print(f'O número 9 foi digitado {tupla.count(9)} vez(es)')
if 3 in tupla:
    print(f'O número três foi lido na {tupla.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado nenhuma vez!')

print('Os valores pares digitados foram: ', end= '')
for i in range(0, 4):
    if tupla[i] % 2 == 0:
        print(f'{tupla[i]}', end= ' ')
print('\n')
