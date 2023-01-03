#Desafio 98

'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem pesonalizada
'''


from time import sleep

def mostraLinha():
    print('=-=' * 12)

    
def contador(i, f, p):
    if p == 0:
        print(f'Contagem de {i} até {f}, de 1 em 1:')
        if i > f:
            for j in range(i, f, -1):
                print(j)
                sleep(0.1)
        else:
            for j in range(i, f, 1):
                print(j)
                sleep(0.1)
    else:
        if i > f:
            if p > 0:
                print(f'Contagem de {i} até {f}, de {p} em {p}:')
                for j in range(i, f, -p):
                    print(j)
                    sleep(0.1)
            else:
                print(f'Contagem de {i} até {f}, de {p*p} em {p*p}:')
                for j in range(i, f, p):
                    print(j)
                    sleep(0.1)

        else:
            for j in range(i, f, p):
                print(j)
                sleep(0.1)
        

mostraLinha()
print('Contagem de 1 até 10, de 1 em 1:')
for i in range(1, 11):
    print(i)
    sleep(0.1)
print('FIM!')
mostraLinha()

print('Contagem de 10 até 0, de 2 em 2:')
for i in range(10, 0, -2):
    print(i)
    sleep(0.1)
print('FIM!')
mostraLinha()

print('Sua vez agora!')
incio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
mostraLinha()

contador(incio, fim, passo)