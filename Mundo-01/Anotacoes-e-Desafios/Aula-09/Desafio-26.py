#Desafio 26

#Faça um programa que leia uma frase pelo teclado e mostre:

#Quantas vezes aparece a letra "A"
#Em que posição aparece a primeira vez
#Em que posição ela aparece pela última vez

frase = str(input('Digite uma frase qualquer: ')).strip()#.upper()
tamFrase = len(frase)
indice = 0
ultimo = 0

while(indice < tamFrase):
    if(frase[indice].upper() == 'A'):
        ultimo = indice
    indice = indice + 1

print('A letra "A" aparece {} vez(es)'.format(frase.upper().count('A')))
print('A letra "A" aparece pela primeira vez no índice {}'. format(frase.upper().find('A') + 1))
print('A letra "A" aparece pela última vez no índice {}'. format(ultimo + 1))
#print('A letra "A" aparece pela última vez no índice {}'. format(frase.upper().rfind('A') + 1))
