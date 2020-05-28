''' 
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
print("=========== desafio 057============")
sexo = input('Digite o sexo com "M" ou "F": ').upper()
while sexo not in 'MF':
    sexo = input('Sexo inválido, digite "M" ou "F": ').upper()
print('Sexo {} registrado com sucesso!'.format(sexo))
