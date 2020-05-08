''' 
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
print("=========== desafio 032============")
ano = int(input('Informe o ano a ser verificado: '))
if ano % 4 == 0:
    if ano % 100 > 0:
        print('É bissexto' )
else:
    if ano % 400 == 0:
        print('É bissexto')        
    else:
        print('Não é Bissexto')
