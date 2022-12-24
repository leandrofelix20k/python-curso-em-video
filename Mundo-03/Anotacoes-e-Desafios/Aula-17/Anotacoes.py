#Listas

#Diferente das tuplas, as listas são multáveis

#O comando .append, adiciona determinado elemento no final da lista
listas = [0, 1, 2, 3]
listas.append(4)
print(f'Comando append: {listas}')

#Já o comando .insert, adiciona mais um espaço em uma determinada posição e insere um novo elemento
listas.insert(0, -1)
print(f'Comando insert: {listas}')

#Apagar um elemento
del listas[1]
print(f'Comando del: {listas}')

#Apagar um elemento com o comando .pop
listas.pop(0)
print(f'Comando pop: {listas}')
#Caso não indicar o indice (listas.pop()), ele removerá o último elemento

#O comando .remove apaga um elemento precisando indicar apenas qual é o elemento.
listas.remove(4)
print(f'Comando remove: {listas}')
#Caso remover um elemento não esteja na lista, será retornado um erro

#Outra forma de criar uma lista
numeros = list(range(2, 15))
print(f'Outro tipo de lista: {numeros}')

#Colocar números em ordem crescente
valores = [3, 8, 5, 6, 14, 11, 16, 12, 19]
valores.sort()
print(f'Ordem Crescente: {valores}')
#Colocar números em ordem decrescente
valores.sort(reverse=True)
print(f'Ordem Decrescente: {valores}')

#Atribuindo valores de uma lista a outra
a = [2, 4, 6, 10]
b = a
print(a)
print(b)
#Ao fazer alterações em uma lista que foi atribuida a partir de outra, a lista atribuidora também será alterada
b[3] = 8
print(a)
print(b)

#Para evitar, deve-se criar uma cópia
c = b[:]
c[0] = 1
print(b)
print(c)
