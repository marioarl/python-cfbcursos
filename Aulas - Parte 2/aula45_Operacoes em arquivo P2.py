
nome = 'teste.txt'
f = open('Aqui deve conter o caminho do arquivo' + nome, 'rt')

print(f.read(10)) # Le os 10 primeiros caracteres do arquivo


f.close()

print('===================================')

nome2 = 'teste2.txt'
g = open('Aqui deve conter o caminho do arquivo' + nome2, 'rt')
print(g.readline()) # Le 1 linha de cada vez do arquivo

#Utilizando o comando FOR para ler linha a linha do arqquivo
for l in g:
    print(l)
g.close()

print('===================================')

#Colocando o resultado da leitura do arquivo em uma variavel
import re #utilizando REGEX
nome3 = 'teste3.txt'
h = open('Aqui deve conter o caminho do arquivo' + nome3, 'rt')

#Substituindo todos os espaços por traço com REGEX
res2 = re.sub(' ', '-', h.readline())
h.close()
print(res2)

#Escrever o retorno da variável res2 dentro do arquivo teste3.txt, mas sem apagar os dados do aqruivo

h = open('Aqui deve conter o caminho do arquivo' + nome3, 'at')
h.write(f'{res2}')
h.close()



