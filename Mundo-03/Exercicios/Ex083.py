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
ultimoParenteseAberto = ultimoParenteseFechado = 0
for j in range(0, len(expressao)):
    if expressao [j] == '(':
        contParentesesAberto += 1
        ultimoParenteseAberto = j
    elif expressao[j] == ')':
        contParentesesFechado += 1
        ultimoParenteseFechado = j

if contParentesesAberto == contParentesesFechado:
    if ultimoParenteseFechado > ultimoParenteseAberto and expressao[0] == '(':
        print('Sua expressão é válida!')
    else:
        print('Sua expressão é inválida!')
else:
    print('Sua expressão é inválida!')


#Outra solução:
'''
expressaoStr = str(input('Digite uma expressão matemática: '))
pilha = []

for simbolo in expressaoStr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
'''