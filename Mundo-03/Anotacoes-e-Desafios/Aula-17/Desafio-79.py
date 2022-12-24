#Desafio 79

'''
Crie um programa onde o usuário possa digitar vários valores númericos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será 
adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
'''

numeros = []

while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)

    while True:
        resp = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
        if resp == 'S' or resp == 'N':
            break
        else:
            print('Tente novamente...', end= '')
    if resp == 'N':
        break

numeros.sort()    
print(f'Lista em ordem crescente: {numeros}')
