''' 
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
print("=========== desafio 036============")
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
tempo = float(input('Em quandos anos pretende pagar? '))
limite = salario * (30/100)
prestacao = valor / (tempo * 12)
print(54*'=-'+'=')
if prestacao <= limite:
    print('\033[1;32;40mEmpréstimo aprovado com valor da prestação de R$ {:.2f}, para pagamento em {:.0f} meses!\033[m'.format(prestacao, tempo * 12))
else:
    print('\033[1;31;40mEmpréstimo negado, valor da prestação de R$ {:.2f} excede o limite de R$ {:.2f} (30%) do salário informado!\033[m'.format(prestacao, limite))
