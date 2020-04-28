# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
print("=========== desafio 020 ============")
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
ordem = random.sample([a1, a2, a3, a4], k=4)
print('1º - '+ ordem[0])
print('2º - '+ ordem[1])
print('3º - '+ ordem[2])
print('4º - '+ ordem[3])