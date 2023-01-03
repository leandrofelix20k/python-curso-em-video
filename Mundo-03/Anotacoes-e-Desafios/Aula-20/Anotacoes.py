#Funções P1

#Estrutura:
def soma(A, B):
    c = A + B
    return c


a = 3
b = 5
print(soma(a, b))

#Empacotamento de parâmetros:
def contador(*numeros):
    print(numeros) #tuplas


contador(1, 5, 2, 7)
contador(4, 2)

#Trabalhando com listas:
def dobra(lista):
    for i in range(0, len(lista)):
        lista[i] *= 2
    '''
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    '''


valores = [1, 2, 3, 4, 5, 6, 7]
dobra(valores)
print(valores)
