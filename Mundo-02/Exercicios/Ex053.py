#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. Desconsiderando os espaços.

frase = str(input('Escreva uma palavra: '))
fraseFormatada = frase.strip().upper().replace(" ", "")
tamPalavra = len(fraseFormatada) 

cont = 0
j = tamPalavra-1
for i in range(0, tamPalavra):
    if(fraseFormatada[i] == fraseFormatada[j]):
        cont += 1
    j -= 1

if(cont == tamPalavra):
    print('A frase "{}" é um palíndromo!'.format(frase))
else:
    print('A frase "{}" não é um palíndromo'.format(frase))


'''
palavra = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(tamPalavra, -1, -1):
    inverso += junto(letra)
if inverso = junto:
    print('Palíndromo')
'''