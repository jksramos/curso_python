a = 'A'
b = 'B'
c = 1.1

# Identifica o valor da {} pelo indice - a ordem importa
formato_1 = 'a={} b={} c={}'.format(a, b, c)

string = 'a={} b={} c={}'
formato_2 = string.format(a, b, c)



print(formato_1)
print(formato_2)