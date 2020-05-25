''' 
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
peso lidos.
'''
print("=========== desafio 055============")
peso = []
for x in range(1, 6):
    print(x, end=' - ')
    peso.append(int(input('Informe o peso: ')))
peso.sort()
print('Menor peso: ', peso[0])
print('Maior peso: ', peso[4])