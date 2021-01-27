''' 
Exercício Python #077 - Contando vogais em Tupla:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
print("== Exercício Python #077 - Contando vogais em Tupla ==")
palavras = ('thiago', 'sousa', 'sofia', 'karolina')

for palavra in palavras:
    print(f'\nVogais de {palavra.upper()}: ', end='')    
    for letra in palavra:  
        if letra.lower() in 'aeiou':
            print(letra, end=' ')