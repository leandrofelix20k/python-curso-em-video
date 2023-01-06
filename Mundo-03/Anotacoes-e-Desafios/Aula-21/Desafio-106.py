#Desafio 106

'''
Faça um mini-sistema que utilize o Interactive Help do python.
O usuário vai digitar o comando e o manual vai aparecer. Quando
o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: Use cores
'''

from time import sleep

while True:
    print('\033[1;30;42m-\033[m' * 50)
    print('\033[1;30;42m-' * 17, '\033[1;30;42mSistema PyHelp', '\033[1;30;42m-\033[m' * 17)
    print('\033[1;30;42m-\033[m' * 50)

    func = str(input('Função ou Biblioteca > ')).lower().strip()
    if func == 'fim':
        break
    
    print('\033[1;30;41m-\033[m' * 50)
    print('\033[1;30;41m-' * 8, f'\033[1;30;41mAcessando manual do comando {func}', '\033[1;30;41m-\033[m' * 8)
    print('\033[1;30;41m-\033[m' * 50)

    sleep(1)
    print(f'\033[1;30;43m{help(func)}\033[m')
    sleep(2)

print('\033[1;30;41m-\033[m' * 50)
print('\033[1;30;41m-' * 20, '\033[1;30;41mATÉ LOGO', '\033[1;30;41m-\033[m' * 20)
print('\033[1;30;41m-\033[m' * 50)