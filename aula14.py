a = 'A'
b = 'B'
c = 1.1

# Identifica o valor da {} pelo indice - a ordem importa
formato_1 = 'a={} b={} c={:.2f}'.format(a, b, c)

string = 'a={} b={} c={:.2f}'
formato_2 = string.format(a, b, c) # tbm pode ser escrito dessa forma

# O indice está especificado nas {} - a ordem não faz diferença
formato_3 = 'b={1} a={0} c={2:.2f}'.format(a, b, c)

formato_4 = 'b={nome2} c={nome3:.2f} a={nome1}'.format(
    nome1=a, nome2=b, nome3=c
)

print(formato_1)
print(formato_2)
print(formato_3)
print(formato_4)