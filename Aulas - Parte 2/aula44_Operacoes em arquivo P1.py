"""
Operacoes em arquivos P1
"""

#Colocar em uma variavel e o metodo open() pede 2 parametros 1o. o arquivo que deseja abrir 2o. o modo de abertura do arquivo r= read(leitura) a=append (adiciona) w=write(escrita) x=create(criacao) t=text(texto) b=binary(binario)

#Abaixo criamos uma variavel com o nome do arquivo e no metodo open() concatenamos com o caminho onde o arquivo deve ficar e utilizamos o modo x para criar o arquivo
nome = "teste.txt"
f=open('Aqui deve conter o caminho do arquivo' + nome, "x" )

#O modo w(write), também cria o arquivo caso ele não exista
nome2 = "teste2.txt"
g=open('Aqui deve conter o caminho do arquivo' + nome2, "w" )

#Neste momento o arquivo teste2.txt já está aberto para a escrita e vamos escrever dentro do arquivo
g.write('CFB Cursos')

'''
IMPORTANTE: Se formos executar novamente este programa e alterarmos o texto do comando g.write() para outro texto, o programa passará  por cima do que estava escrito e colocara o novo texto, porque não abrimos o arquivo em modo APPEND (linha 13) ele está aberto em modo WRITE
'''
#É muito importante ao final fechar o aqruivo
g.close()

