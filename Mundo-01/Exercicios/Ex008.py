#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

value = float(input('Digite um valor: '))

cm = value * 100
mm = value * 1000

print('{:.1f} metros convertido em centímetros: {:.2f}, milímetros: {:.2f}'.format(value, cm, mm))