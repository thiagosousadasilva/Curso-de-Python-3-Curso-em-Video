''' 
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''
print("=========== desafio 027 ============")
nome = input('Digite o nome da pessoa: ')
lsnome = nome.split()
print("""
Primeiro nome: {}
Último nome: {}
""".format(lsnome[0].capitalize(), lsnome[len(lsnome)-1].capitalize()))