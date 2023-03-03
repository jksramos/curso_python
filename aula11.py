# 1. (n + n) -> Parenteses sempre vem primeiro ((Os internos tem preferência)).
# 2. ** -> Potenciação
# 3. * / // % -> Multiplicação, Divisão, inteiro da divisão e módulo
# 4. + - -> Adição e subtração

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)