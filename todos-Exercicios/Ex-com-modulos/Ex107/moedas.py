def aumentar(moeda, porcentagem):
    res = moeda + moeda * (porcentagem / 100)
    return res

def diminuir(moeda, porcentagem):
    res = moeda - moeda * (porcentagem / 100)
    return res

def dobro(moeda):
    res = moeda * 2
    return res

def metade(moeda):
    res = moeda / 2
    return res
    