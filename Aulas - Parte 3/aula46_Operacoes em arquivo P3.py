import os
nome = 'teste.txt'
caminho = 'Aqui deve conter o caminho do arquivo'
f = open(caminho + nome, 'x')
f.close()

#Apagando o arquivo
os.remove(caminho + nome)

print('==========================')

#Se o arquivo já existir, informar ao usuario
nome2 = 'teste2.txt'
if os.path.exists(caminho + nome2):
    print('Arquivo existente')
else:
    g = open(caminho + nome2, 'x')
    print('Arquivo criado')
    g.close()