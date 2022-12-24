#Desafio 80

'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e 
cadastre-o em uma lista, já na posição correta de inserção(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''

print('Digite cinco valores: ')
valores = []

for i in range(0, 5):
    valores.append(int(input()))
    cont = 0
    if i == 0:
        print('Primeiro valor adicionado!')
    else:
        for j in range(0, i+1):
            if valores[i] > valores[j]:
                cont += 1
        if cont == i:
            print('Valor adicionado na última posição!')
        else:
            print(f'Valor adicionado na posição {cont}')
            valores.insert(cont, valores[i])
            valores.pop(i+1)
                           
print(valores)
