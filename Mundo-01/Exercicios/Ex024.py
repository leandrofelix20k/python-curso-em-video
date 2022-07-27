#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome da sua cidade: ')).strip()

procurarPalava = cidade.upper().find('SANTO')

if(procurarPalava == 0):
    print('O nome da sua cidade começa com a palavra "Santo"!')
else: 
    print('O nome da sua cidade não começa com a palavra "Santo"!')
    