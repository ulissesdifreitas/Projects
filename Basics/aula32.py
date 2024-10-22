"""
Exercício 01 ----

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

Exercício 02 ----

Faça um programa que pergunte a hora ao usuário e, baseado-se no horário
descrito, exiba a saudação apropriada:
Ex. Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.

Exercício 03 ----

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

# Exercício 01
numero_int = input("Digite um número inteiro: ")

if '.' in numero_int:
    print(f"{numero_int} não é número inteiro!")
else:
    print(f"Você digitou o número inteiro {numero_int}")

#Exercício 02

hora_certa = int(input("Que horas são?: "))


if hora_certa >= 0 and hora_certa <= 11:
    print("Bom dia")

elif hora_certa >= 12 and hora_certa <=17:
    print("Boa tarde")

elif hora_certa >= 18 and hora_certa <= 23:
    print("Boa noite")

else:
    print('Você não digitou uma hora válida')


#Exercício 03

nome_usuario = input('Digita seu primeiro nome: ')

if len(nome_usuario) <= 4:
    print("Seu nome é curto")

elif len(nome_usuario) == 5 or len(nome_usuario) == 6:
    print("Seu nome é normal")

else:
    print("Seu nome é muito grande.")