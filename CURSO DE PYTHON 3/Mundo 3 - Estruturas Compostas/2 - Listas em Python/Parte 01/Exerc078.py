''' 
Exercício Python #078 - Maior e Menor valores na Lista:
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
'''
print("== Exercício Python #078 - Maior e Menor valores na Lista ==")
valores = []
for n in range(0,5):
    valores.append(int(input(f'{n+1}º valor: ')))
val_ordenados = valores[:]
val_ordenados.sort()
print(f'O "{val_ordenados[-1]}" foi o maior valor, na posição "{(valores.index(val_ordenados[-1])+1)}".')
print(f'O "{val_ordenados[0]}" foi o menor valor, na posição "{(valores.index(val_ordenados[0])+1)}".')