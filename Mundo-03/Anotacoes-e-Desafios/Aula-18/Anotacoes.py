#Listas Aula-18

#Listas dentro de listas:
pessoas = []
pessoa1 = ['João', 25]
pessoa2 = ['Maria', 32]

pessoas.append(pessoa1[:])
pessoas.append(pessoa2[:])
print(pessoas)
del(pessoas)

#Outra forma:
pessoas = [['Pedro', 19], ['Chico', 45]]
print(pessoas)
print(pessoas[1])
print(pessoas[0][0])
pessoas[0][0] = 'Raúl'
print(pessoas)
pessoas.append(pessoa1[:])
print(pessoas)

#Imprimindo a lista
print('--' * 20)
for i in range(0, 3):
    print(pessoas[i][0])

#Lendo elemento e adicionando em uma lista e a colocando em outra
print('--' * 20)
grupo = list()
dado = list()
for j in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    grupo.append(dado[:])
    dado.clear()
