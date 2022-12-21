#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com s média atingida.
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('SUa média foi: {}'.format(media))

if(media < 5.0):
    print('REPROVADO! MÉDIA INFERIOR A 5.0')
elif(media >= 5.0 and media < 7):
    print('RECUPERAÇÃO! VAMOS QUE DÁ!')
else: 
    print('APROVADO! FOGUETE NÃO TEM RÉ!')
    