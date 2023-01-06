#Funções P2


#Comando help é utilizado para entender como funciona algumas funções

#help(print)

#Criando uma docstring para funções próprias:

def soma(a=0, b=0):#Adiona o zero após o parâmetro, torna opcional a passagem de valores
    """
    -> Retorna a soma de dois valores
    :parâmetro a: Primeiro valor
    :parâmetro b: Segundo valor
    :return: Retorna a soma de a e b
    """
    c = a + b
    print(c)

    return c


soma(1)
soma(2, 4)

#Escopo de variáveis:
def teste(b):
    #O comando 'global' serve para tratar determinada variável como global
    global a
    #Váriavel local
    b += 5
    print(f'b = {b}')
    #print(f'É possivel utilizar a variável a = {a} aqui')
    #Criando uma variável local para a
    #a = 10
    #print(f'O valor local de a = {a}')
    a = a + b


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


#Variável Global
a = 3
teste(a)
print(f'a = {a}')

num = int(input('Digite um número: '))

if par(num):
    print('É par!')
else:
    print('É ímpar!')
    