#Em Python, existe apenas duas estruturas de repetição que são:
#For e While.

#Laço infinito:

'''
while True:
    print('Eu não vou enviar banha pelo correio.')
'''

#O comando break:

'''
cont = 0
while True:
    print(cont)
    cont += 1
    if cont == 100:
        break
print('FIM!')
'''

#fstrings

x = 100
y = 89

print(f'A soma de x com y é igual à {x+y}')