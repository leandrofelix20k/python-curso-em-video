#Desafio 102

'''
Crie um programa que tenha uma função que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial. 
'''

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :parâmetro n: O número a ser calculado
    :parâmetro show: (opcional) Mostrar ou não o cálculo
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            if i > 1:
                print(f'{i} x ', end= '')
            else:
                print(f'{i} = ', end= '')
        f *= i
    
    return f


print(fatorial(5, show=True))

#help(fatorial)
