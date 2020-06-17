''' 
Exercício Python #105 - Analisando e gerando Dicionários:
Faça um programa que tenha uma função notas() que pode receber várias notas 
de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''
print("== Exercício Python #105 - Analisando e gerando Dicionários ==")
from math import trunc
def notas(*notas, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos
    :param sit: valor opcional, quando True será adicionada a situação das notas
    :return: dicionário com várias informações sobre a turma
    """
    listagem = {}
    listagem['Qtd_Notas'] = len(notas)
    media = round(sum(notas)/len(notas), 2)
    listagem['Maior_nota'] = max(notas)
    listagem['Menor_nota'] = min(notas)
    listagem['Média'] = media
    if sit == True:
        if media <= 5:
            listagem['Situação'] = 'Ruim'
        elif 5 >  media < 7:
            listagem['Situação'] = 'Regular'            
        elif media > 7:
            listagem['Situação'] = 'Boa'            
    return listagem
resp = notas(9, 7.8, 5, 8)
print(resp)