'''
Faça um programa que mostre a tabuada de vários números, um de
cada vez, para cada valor digitado pelo usuário. O programa 
será intermpido quando o número solicitado for negativio
'''

while True:
    num = int(input('Deseja a tabuada de qual número? '))
    if num < 0:
        break
    print('-' * 5, f'TABUADA DO NÚMERO {num}', '-' * 5)
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')
    print('\n')

print('PROGRAMA ENCERRADO! VOLTE SEMPRE!')