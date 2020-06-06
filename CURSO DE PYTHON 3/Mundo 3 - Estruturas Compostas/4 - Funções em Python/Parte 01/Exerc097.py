''' 
Exercício Python #097 - Um print especial:
Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''
print("== Exercício Python #097 - Um print especial ==")
def escreva(x):
    y = len(x) + 4
    print('-'*y)
    print(f'{x.title():^{y}}')
    print('-'*y)

texto = input('Digite o texto para ser formatado: ')
escreva(texto)