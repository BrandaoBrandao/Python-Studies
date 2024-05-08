# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdareia avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# 0 0.0 '' False
# Também existe o tipo None que é
# usado apra representar um não valor

#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')
#senha_permitida = '123'
#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrou')
#else:
#     print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)