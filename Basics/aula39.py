"""
Iterando strings com while

"""

# 0123456789

nome = "Ulisses Freitas"

tamanho_do_nome = len(nome)
print(nome)
print(tamanho_do_nome)
indice = 0

while indice < tamanho_do_nome:
    print(nome[indice])
    indice += 1