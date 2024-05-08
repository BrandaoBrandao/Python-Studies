"""
Iterando strings com while
"""
#       012345678910
nome = 'Fernando Brandão' # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
contador = 0
nova_string = '*'

while contador < tamanho_nome:
    letra = nome[contador] 
    contador += 1
    nova_string += letra + '*'

print(nova_string)