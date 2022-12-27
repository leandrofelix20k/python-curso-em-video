'''
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares.No final, mostre os valores em ordem crescente.
'''

valor = 0
paresAndImpares = [[], []]

print('Digite 7 números: ')
for i in range(0, 7):
    valor = int(input())

    if valor % 2 == 0:
        paresAndImpares[0].append(valor)
    else:
        paresAndImpares[1].append(valor)

paresAndImpares[0].sort()
paresAndImpares[1].sort()
print(f'Número pares: {paresAndImpares[0]}')
print(f'Número ímpares: {paresAndImpares[1]}')
