# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso a expressão inteira
# será avaliada naquele valor
# São considerados falsy
# 0 0.0 '' False
# Também existe o tipo None que ie usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123'
if entrada == 'E' and senha_digitada == senha_permitida:
     print('Entrou')
else:
     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)