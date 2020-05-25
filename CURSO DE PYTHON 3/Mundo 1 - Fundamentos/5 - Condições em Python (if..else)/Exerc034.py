''' 
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250 calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
print("=========== desafio 034============")
sal = float(input('Informe o valor do salário: '))
if sal <= 1250:
    print('O salário terá um aumento de 15%, sendo R$ {:.2f}, totalizando R$ {:.2f}'.format(sal * 0.15, sal + (sal * 0.15)))
else:
    print('O salário terá um aumento de 10%, sendo R$ {:.2f}, totalizando R$ {:.2f}'.format(sal * 0.1, sal + (sal * 0.1)))