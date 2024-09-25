nome = 'Ulisses'
peso = 120
altura = 1.75
imc = peso / (altura * altura) 

# IMC = peso / (altura x altura)

print('O', nome, 'tem', altura, 'de altura, pesa ', peso, 'quilos e seu imc é ', imc)

# Uma dica sobre f-strings

print(f'O {nome} tem {altura} de altura, pesa {peso} quilos e seu imc é {imc:.2f}')