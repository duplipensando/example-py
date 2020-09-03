'''
>>>>>tipos de string
inicializar: '', "", 3 aspas
concatenar: +  e *

>>>>>>métodos
a = abacadabra
a.count('a') #4
a.partition('c') #('abra', 'c', 'adabra') retorna uma tupla
a.lower() #'abacadabra'
a.index('c') #4
a.replace('a', 'c') #'abrcccdcbrc'
a.split('a') #['abra', 'c'. 'd', 'br', ''] retorna uma lista

>>>>>>formatar string

nome = 'pao'; idade = 3
F-string
f'nome: {nome}, idade:{idade}'   #retorna: 'nome: pao, idade:3'

str.format()
'nome:{}, idade{}'.format(nome, idade)   #retorna: 'nome:pao, idade:3'

estilo antigo
'nome:%s,idade:%s'%(nome, idade)    #retorna: 'nome: pao, idade:3'
'''
# 'a' em abacadabra retorna um booleano: true

#in de pertercimento
msg = 'pao fede a bosta'
if 'fede' in msg:
    print('ih fede mesmo')
else:
    print('jamais anjo chereisa')
