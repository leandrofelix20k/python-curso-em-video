def moeda(moeda):
    return (f'R${moeda:.2f}')


def aumentar(moeda, porcentagem):
    return moeda + moeda * (porcentagem / 100)


def diminuir(moeda, porcentagem):
    return moeda - moeda * (porcentagem / 100)


def dobro(moeda):
    return moeda * 2


def metade(moeda):
    return moeda / 2