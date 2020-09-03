'''
++estruturas de decisão
if, elif, else

parenteses não são necessários, nem memso com conectivos: if x>y or x<y
'''
x = 7
y = 5
if x == y:
    print('mesmo valor')
elif x > y:
    print('x é maior que y')
else:
    print(f'Não sei resolver {x} e {y}')

    carteira = int(input('Quanto eu tenho?  '))
    bolsa = int(input('Quanto custa a bolsa?  '))
    necessidade = input('Preciso mesmo disso [s/n]?   ')

    if carteira >= bolsa and necessidade == 's':
        print(' e bueno vo compra')
    else:
        print('parece q não')
'''
        condições falsas
0: false
false: false
none: false
não entrará no bloco ex:

        condições falsas: sequências vazias
''
{}
[]
if []:
não entrará no bloco
'''
