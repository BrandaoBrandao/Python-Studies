"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

# lista = ['Maria', 'Helena', 'Luiz']
# cont = 0

# for nome in lista:
#     print(cont, nome)
#     cont +=1

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])