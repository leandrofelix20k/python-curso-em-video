#Desafio 83

'''
Crie um programa onde o usuário digite uma expressão qualquer que
use parênteses. Seu aplicativo deverá analisar se a expressão 
passada está com os parênteses abertos e fechados na ordem correta.
'''

expressaoStr = str(input('Digite uma expressão matemática: '))
expressao = []

for i in range(0, len(expressaoStr)):
    if expressaoStr[i] == '(' or expressaoStr[i] == ')':
        expressao.append(expressaoStr[i])

contParentesesAberto = contParentesesFechado = 0
indUltimoAberto = indUltimoFechado = 0
for j in range(0, len(expressao)):
    if expressao [j] == '(':
        contParentesesAberto += 1
        indUltimoAberto = j
    elif expressao[j] == ')':
        contParentesesFechado += 1
        indUltimoFechado = j

if contParentesesAberto == contParentesesFechado:
    if indUltimoFechado > indUltimoAberto:
        print('Sua expressão é válida!')
    else:
        print('Sua expressão é inválida!')
else:
    print('Sua expressão é inválida!')
