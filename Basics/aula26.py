"""
Formatação de Strings

s - string
d - int
f - float

.<numero de digitos>f

< - Esquerda
> - Direita
^ - Centro
"""


variavel = "ABC"

print(variavel)
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:^10}.')
print(f'{1000.234234234:.2f}')
