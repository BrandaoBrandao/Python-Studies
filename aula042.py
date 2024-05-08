frase = 'O Python é uma linguagem de programação'\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_que_apareceu_mais = letra_atual
    
    i += 1

print('A letra que aoareceu mais vezes foi '
      f'"{letra_que_apareceu_mais}" que apareceu '
      f'{qtd_apareceu_mais_vezes} vezes')