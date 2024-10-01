"""
Interpolação básica de Strings

s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

"""

nome = "Ulisses"
preco = 1000.987675123
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (1500, 1500))