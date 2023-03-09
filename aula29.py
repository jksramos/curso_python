"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que vc digitar: ')

try:
    num_float = float(numero_str)
    print(f'O dobro de {numero_str} é {num_float * 2:.2f}')
except:
    print('Isso não é um numero')

print(20 * '-') # --------------------

num_str = input('Vou dobrar o número que vc digitar novamente: ')

if num_str.isdigit():
    nunero_float = float(num_str)
    print(f'O dobro de {num_str} é {nunero_float * 2:.2f}')
else:
    print('Isso não é um numero')