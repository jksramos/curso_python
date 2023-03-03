nome = 'Jackson Ramos'
altura = 1.71
peso = 72
imc = 72 / 1.71 ** 2

# Formatação de strings usando "f-strings"
# ":.2f" define a quantidade de casas decimais após o ponto flutuante
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}.'

print(linha_1)
print(linha_2)
print(linha_3)

# Jackson Ramos tem 1.71 de altura
# pesa 72 quilos e seu IMC é
# 24.622960911049557