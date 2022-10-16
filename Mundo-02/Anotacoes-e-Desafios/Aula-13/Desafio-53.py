#Desafio 53

#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. Desconsiderando os espaços.

frase = str(input('Escreva uma palavra: '))
fraseFormatada = frase.strip().upper().replace(" ", "")
tamPalavra = len(fraseFormatada) 

cont = 0
j = tamPalavra-1
for i in range(0, tamPalavra):
    if(fraseFormatada[i] == fraseFormatada[j]):
        j -= 1
        cont += 1

if(cont == tamPalavra):
    print('A frase "{}" é um palíndromo!'.format(frase))
else:
    print('A frase "{}" não é um palíndromo'.format(frase))
