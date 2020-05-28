''' 
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor 
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
'''
print("=== Exercício Python #067 - Tabuada v3.0 ====")
while True:
    n = int(input('Digite um número inteiro (ou um nº negativo para sair): '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')