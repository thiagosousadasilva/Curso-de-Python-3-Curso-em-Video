''' 
Crie um programa que leia o nome completo de uma pessoa e mostre:
    - o nome com todas as letras maiúsculas.
    - o nome com todas minúsculas.
    - quantas letras ao todo (sem considerar espaços).
    - quantas letras tem o primeiro nome.
'''
print("=========== desafio 022 ============")
nome = input('Informe o nome completo: ')
lsnome = nome.split()
lsnome = ''.join(lsnome)
print("""
Maiúsculas: {}
Minúsculas: {}
Letras ao todo (sem considerar espaços): {}
Letras do primeiro nome: {}
""".format(nome.upper(),nome.lower(),len(lsnome), len(lsnome[0])))