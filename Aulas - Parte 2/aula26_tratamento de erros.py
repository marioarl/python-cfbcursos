#Try Except = Verificar se o bloco de comandos está com algum erro, gera um exceçao e cai no Except
x = 10
try: #
    print(x)
except NameError:# Except irá retornar só se o Try tiver algum erro, except é obrigatorio
    print("X não está definido")
except:
    print("Erro desconhecido")
else: # Else não é obrigatório
    print('Tudo certo')
finally: # Finaly vai retornar se Try tiver um erro ou não, Finally não é obrigatorio
    print('Fim do tratamento')


# utilizando o comando raise Exception
num = -10 #Não permitir que o valor de num fique abaixo de 1
if num < 1:
    raise Exception('Valor não permitido')

#Verificando o tipo da veriavel
num1 = "Bruno"
if not type(num1) is int:
    raise Exception("Somente numeros permitidos")
else: 
    print(num1)