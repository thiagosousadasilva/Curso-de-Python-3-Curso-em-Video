''' 
Exercício Python #083 - Validando expressões matemáticas:
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
abertos e fechados na ordem correta.
'''
print("== Exercício Python #083 - Validando expressões matemáticas ==")
lista = []
lista += input('Digite a expressão: ')
if lista.count('(') == lista.count(')'):
    print('Parenteses CORRETOS!')
else:
    print('Parenteses INCORRETOS.')
