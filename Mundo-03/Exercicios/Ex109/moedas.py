def moedas(m):
    return (f'R${m:.2f}')


def aumentar(moeda, porcentagem, form=False):
    moeda = moeda + moeda * (porcentagem / 100)

    if form:
        return moedas(moeda)

    return moeda


def diminuir(moeda, porcentagem, form=False):
    moeda = moeda - moeda * (porcentagem / 100)

    if form:
        return moedas(moeda)

    return moeda


def dobro(moeda, form=False):
    moeda = moeda * 2

    if form:
        return moedas(moeda)

    return moeda


def metade(moeda, form=False):
    moeda = moeda / 2

    if form:
        return moedas(moeda)

    return moeda
