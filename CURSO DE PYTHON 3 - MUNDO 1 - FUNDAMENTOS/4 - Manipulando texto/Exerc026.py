''' 
Faça um programa que leia uma frase pelo teclado e mostre:
    - quantas vezes aparece a letra "A".
    - em que posição ela aparece a primeira vez.
    - em que posição ela aparece a última vez.
'''
print("=========== desafio 026 ============")
frase = input('Digite a frase: ').lower()
print("""
Total de letras 'A': {}
Posição de ocorrências:
- Primeira: {}
- Última: {}
""".format(frase.count('a'), frase.find('a'), frase.rfind('a')))