"""
Try / Except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar 
"""

numero = input('Vou dobrar o número que você digitar: ')

try:
    num_int = int(numero)
    print(f'O dobro de {num_int} é {num_int * 2}')
except:
    print("Digite apenas números")


"""Utilizando IF/ELSE"""
# if numero.isdigit():
#     num_int = int(numero)
#     print(f'O dobro de {num_int} é {num_int * 2}')     
# else:
#     print("Digite apenas números")