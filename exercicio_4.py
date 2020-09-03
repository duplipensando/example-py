"""
faça um programa que peça 2 números inteiros e um número float.
calcule e mostre:
o produto do dobro do primeiro com metade do segundo
a soma do triplo do primeiro com o terceiro
o terceiro elevado ao cubo

++int colocado para transformar o valor do input em inteiro pois ele armazena string
++tipos numéricos:
int
float
complex
++operadores
+
-
*
** potência
/
// dividir sem sobrar
% resto da divisão

toda operação de inteiro, retorna um inteiro, mas se o resultado for quebrado transforma em float
toda operação de float retorna float
toda operação com complexos retorna complexos
"""
numero_1 = int(input('digite um número inteiro'))
numero_2 = int(input('digite outro número inteiro'))
numero_3 = float(input('digite um número float'))

resultado_1 = (numero_1 * 2) * (numero_2 /2)
print(f'Resultado 1: {resultado_1}')

resultado_2 = (numero_1 * 3) + numero_3
print(f'Resultado 2: {resultado_2}')

resultado_3 = numero_3 ** 3
print(f'Resultado 3: {resultado_3}')
