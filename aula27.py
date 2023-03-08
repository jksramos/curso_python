"""
Fatiamento de Strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[0:]) # Olá mundo
print(variavel[0:6]) # Olá mu
print(variavel[:9]) # Olá mundo
print(variavel[0:9:2]) # Oámno
print(variavel[::-1]) # odnum álO
print(10 * '-')
print(len(variavel))



