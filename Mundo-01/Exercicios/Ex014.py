#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

tempC = float(input('Digite a temperatura em °C: '))

convertF = tempC * 1.8 + 32

print('A temperatura {:.1f}°C em Fahrenheit é de {:.1f}°F'.format(tempC, convertF))