''' 
Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, 
cobrando R$ 0,50 por KM para viagens de até 200km e R$ 0,45 para viagens mais longas.
'''
print("=========== desafio 031============")
d = float(input('Digite a distância da viagem: '))
if d<= 200:
    print('Valor da passagem R$ {:.2f}'.format(d * 0.50))
else:
    print('Valor da passagem R$ {:.2f}'.format(d * 0.45))