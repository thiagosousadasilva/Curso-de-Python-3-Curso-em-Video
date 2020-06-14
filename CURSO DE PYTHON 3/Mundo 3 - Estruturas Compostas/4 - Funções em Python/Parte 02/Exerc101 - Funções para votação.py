''' 
Exercício Python #101 - Funções para votação:
Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um valor 
literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
print("== Exercício Python #101 - Funções para votação ==")
from datetime import date
def voto(ano_nasc):
    idade = date.today().year - ano_nasc
    if idade < 16:
        return f'\n\033[1;31m Com {idade} anos: Não Vota!\033[m\n'
    elif 16 <= idade < 18 or idade >= 65:
        return f'\n\033[1;32m Com {idade} anos: Voto Opcional.\033[m\n'
    elif 18 <= idade < 65:
        return f'\n\033[1;34m Com {idade} anos: Voto Obrigatório.\033[m\n'

print(voto(int(input('Informe o ano de nascimento: '))))