# Conversão de tipos, coerção
# type convertion, typecasting, coercion
"""
é o ato de converter um tipo em outros tipos imutáveis e primitivos:
str, int, float, bool
"""
print(int('1') + 1, type(int('1'))) # str ('1') em int
print(float('1') + 1, type(float('1'))) # str ('1') em float
print(bool(' '), type(bool(' '))) # str (' ') em bool "nesse caso há um caracter dentro"
print(bool(''), type(bool(''))) # str ('') em bool "nesse caso não há caracter dentro"
print(str(1) + 'a', type(str(1))) # int (1) em str
