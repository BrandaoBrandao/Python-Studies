"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')

        item = input('Insira o item: ')
        lista.append(item)

    elif opcao == 'a':
        indice = input('Insira o indice do item a ser apagado: ')

        try:
            indice = int(indice)
            del lista[indice - 1]
        except ValueError:
            print('Por favor digite um número inteiro')
        except IndexError:
            print('Indice não existente')
        except Exception:
            print('Erro desconhecido')        

    elif opcao == 'l':
        os.system('cls')

        if lista == []:
            print('Sua lista está vazia')
        else:
            for codigo, itens in enumerate(lista, start = 1):
                print(codigo, itens)
    else:
        print('Opção inválida')

