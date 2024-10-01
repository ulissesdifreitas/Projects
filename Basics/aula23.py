# Operadores in e not in
# Strings são iteráveis 
# 0 1 2 3 4 5 6
# U L I S S E S
#-7-6-5-4-3-2-1
nome = "ULISSES"
print(nome[2])
print(nome[-5])

print("X" not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')