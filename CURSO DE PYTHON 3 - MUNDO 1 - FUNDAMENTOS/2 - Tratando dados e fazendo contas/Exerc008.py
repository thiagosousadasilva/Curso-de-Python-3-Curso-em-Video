# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.
print("=========== desafio 008 ============")
valor = float(input('Informe os valor em metros: '))
print('O valor convertido é de {:.0f} centímetros e de {:.0f} milímetros.'.format(valor*100, valor*1000))