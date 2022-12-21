'''
Crie um programa que tenha uma tupla com várias palavras(não usar
acentos). Depois disso, você deve mostrar, para cada palavra, quais
são as suas vogais.
'''

palavras = ('Para', 'Aprender', 'Programar', 'Python', 'Basta', 
'Praticar')
tamPalavras = len(palavras)

for i in range(0, tamPalavras):
    pala = palavras[i].lower()
    print(f'\nNa palavra {pala.upper()} temos ', end='')
    for j in range(0, tamPalavras):
        if pala[j] in 'aeiou':
            print(f'{pala[j]} ', end= '')
    