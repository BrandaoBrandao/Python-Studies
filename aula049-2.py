"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - Apaga um indice
    claer - Limpa a lista
    extend - Extende a lista
    + - Concatena listas
Create Read Update   Delete = lista[i] (CRUD)
"""

#        0   1   2   3 
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear
lista.insert(100, 5)
print(lista)