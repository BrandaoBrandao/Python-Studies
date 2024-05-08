"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')

try:
    num_int = int(num)
    if num_int %2 == 0:
        print(f'O número {num_int} é par')
    else:
        print(f'O número {num_int} é impar')
except:
    print('Não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_atual = input('Que horas são? ')

try:
    hora_float = float(hora_atual)
    bom_dia = 0 <= hora_float <= 11
    boa_tarde = 12 <= hora_float <= 17
    boa_noite = 18 <= hora_float <= 23.9
    if bom_dia:
        print('Bom dia')
    elif boa_tarde:
        print('Boa tarde')
    elif boa_noite:
        print('Boa noite')
    else:
        print('Você não digitou um horário válido')
except:
    print('Você não digitou um horário válido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(primeiro_nome)

if primeiro_nome:
    if tamanho_nome <= 4:
        print('Seu nome é pequeno')
    elif tamanho_nome <= 6:
        print('Seu nome é médio')
    else:
        print('Seu nome é grande')
else:
    print('Por favor digite seu nome')