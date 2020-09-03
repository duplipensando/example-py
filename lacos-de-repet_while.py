'''
while: enquanto for verdadeiro executar, recebe valor booleano

exemplos:
a) while BOOL:
    do
else:
    do
    #executa o else quando acabar o while, mas não com um break

b) while 3 < 4:
        print('três é menor')

c) while True:
            #??? repete p sempre

d) x =0
   while x > 10:
        x = input('um num:')

'''
resposta = input('bora dá um role [s/n]??   ')
n = 1
while resposta != 's':
    resposta = input(f'bora{'a' * n} [s/n]?   ')
    n += 1
    if 'chato' in resposta or 'chata' in resposta:
        print('foi mal')
        break
else:
    print(f'bora{'a' * n}!!!')
