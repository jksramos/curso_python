"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um numero INTEIRO: ')

if num.isdigit():
    num_int = int(num)
    if (num_int % 2) == 0:
        print('Esse numero é "par"')
    else:
        print('Esse numero é "Impar"')    
else:
    print('Você não digitou um numero INTEIRO')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite a hora em numero Inteiro: ')

if hora.isdigit():
    hora_float = int(hora)
    if hora_float <= 11:
        print('Bom dia!')
    elif (hora_float > 11) and (hora_float <= 17):
        print('Boa tarde')
    elif (hora_float > 17) and (hora_float <= 23):
        print('Boa noite')
    else:
        print('Esse numero não é válido')
else:
    print('Isso não é um dado válido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')
tam_nome = len(nome)

if tam_nome <= 4:
    print('Seu nome é curto')
elif (tam_nome > 4) and (tam_nome <= 6):
    print('Seu nome é normal')
else:
    print('Seu nome é longo')