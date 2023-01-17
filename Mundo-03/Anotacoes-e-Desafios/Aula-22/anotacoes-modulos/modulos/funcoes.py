def fatorial(n):
    f = 1
    for i in range(n, 0, -1):
        f *= i
    
    return f


def parOuImpar(n):
    if n % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'

def dobro(n):
    return n*2