''' 
Crie um programa que leia o nome de uma cidade e diga se ela 
começa ou não com o nome "SANTO".
'''
print("=========== desafio 024 ============")
cidade = input('Digite o nome da cidade: ').split()
print('SANTO' in cidade[0].upper())