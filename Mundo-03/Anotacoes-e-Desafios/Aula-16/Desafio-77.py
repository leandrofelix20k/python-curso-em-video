#Desafio 77

'''
Crie um programa que tenha uma tupla com várias palavras(não usar
acentos). Depois disso, você deve mostrar, para cada palavra, quais
são as suas vogais.
'''

palavras = ('Para', 'Aprender', 'Programar', 'Python', 'Basta', 
'Dedicar')

for i in range(0, len(palavras)):
    pala = palavras[i].lower()
    print(f'\nNa palavra {pala.upper()} temos ', end='')
    for j in range(0, len(palavras[i])):
        if pala[j] in 'aeiou':
            print(f'{pala[j]} ', end= '')