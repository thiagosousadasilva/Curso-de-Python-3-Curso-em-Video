''' 
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto.
- à vista no cartão: 5% de desconto.
- em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.
'''
print("=========== desafio 044============")
preco = float(input('Informe o preço: '))
print('''
1 - à vista dinheiro/cheque: 10% de desconto.
2 - à vista no cartão: 5% de desconto.
3 - em até 2x no cartão: preço normal.
4 - 3x ou mais no cartão: 20% de juros.
''')
condicao = int(input('Qual a opção de pagamento: '))
if condicao == 1:
    print('À vista dinheiro/cheque: 10% de desconto.: R$ {:.2f}'.format(preco - (preco * 10/100 )))
elif condicao == 2:
    print('À vista no cartão: 5% de desconto.: R$ {:.2f}'.format(preco - (preco * 5/100)))
elif condicao == 3:
    print('Preço normal R$ {:.2f} em 2x de R$ {:.2f}'.format(preco, preco/2))
elif condicao == 4:
    ptotal = preco + (preco * 20/100)
    print('Parcelado 3x de R$ {:.2f} com acréscimo de 20% de juros. Total R$ {:.2f}'.format(ptotal/3, ptotal))
else:
    print('Condição de pagamento incorreta.')