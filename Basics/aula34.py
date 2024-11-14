"""
Repetições - Laços de Repetição
while (Enquanto)
Executa uma ação enquanto determinada condição for verdadeira
"""

condicao = True

while condicao:
    nome = input("Qual o seu nome: ")
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')