def leiaDinheiro(moeda):
    while True:
        moeda = str(input(moeda))
        moeda = moeda.replace(',', '.')

        if moeda.replace('.', '').isdigit():
            return float(moeda)
        