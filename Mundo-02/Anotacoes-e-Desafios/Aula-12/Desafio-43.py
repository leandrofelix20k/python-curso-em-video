#Desafio 43

#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Morbida

peso = float(input('Informe seu peso: '))
altura = float(input('informe sua altura: '))
imc = peso / (altura * altura)

print('\nIMC: {:.2f}'.format(imc))
if(imc < 18.5):
    print('Status: ABAIXO DO PESO')
elif(imc >= 18.5 and imc <= 25):
    print('Status: PESO IDEAL')
elif(imc > 25 and imc <= 30):
    print('Status: SOBREPESO')
elif(imc > 30 and imc <= 40):
    print('Status: OBESIDADE')
else:
    print('Status: OBESIDADE MORBIDA')
    