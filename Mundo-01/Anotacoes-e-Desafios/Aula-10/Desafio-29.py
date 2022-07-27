#Desafio 29

#Escreva um programa que leia a velociade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada Km acima da média

velocidade = int(input('Registre a velocidade do carro em Km/h: '))

if velocidade <= 80:
    print('Tudo ok! Você está andando abaixo do limite permitido de 80Km/h')
else:
    multa = (velocidade - 80) * 7
    print('Você foi multado em R${:.2f}, pois ultrapassou o limite de 80Km/h'.format(multa))
    