# \r\n -> CRLF "quebra de linha usada em versões mais antigas do windows"
# \n -> LF "quebra de linha usada nos sistemas baseados em unix"
# sep="" "define o que será usado como separador entre os argumentos da função"
# end="" "define se haverá uma quebra de linha ou qualquer outra coisa entre as linhas de código"
print(12, 34, 1011, sep="-", end='\n##')
print(56, 78, sep='-', end="\n")
print(9, 10, sep='-', end="\n")