'''
faça um programa que receba uma data de nascimento(00/00/0000) e imprima
'você nasceu em <dia> de <mes> de <ano>'
'''

resposta = input('data de nascimento:   ')
#03/04/1994
dia, mes, ano = resposta.split('/')
print(f'eu nasci em {dia} de {mes} de {ano}')
