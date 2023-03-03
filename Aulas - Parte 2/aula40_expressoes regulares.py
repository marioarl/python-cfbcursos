"""
Expressoes Regulares, RegEX são como uma mini liguagem de programação e tem recursos bastante interessantes para trabalhar com STRINGS

"""
#Findall - Serve para encontrar todas as ocorrencias de uma determinada STRING em outra STRING e retorna uma colecao com essa pesquisa

import re #Importando a biblioteca REGEX

texto = 'Curso de Python do CFB Cursos, canal do YouTube'

res = re.findall("Python", texto)# 1o. parametro o que voce quer encontrar / 2o parametro o lugar a ser procurado
print(res)

res = re.findall("so", texto)
print(res)

#ler um valor do teclado e pesquisar na string
pesq = str(input('Pesqisar: ')).strip()
res2 = re.findall(pesq, texto)
print(res2)

#Saber a quantidade de elementos
qtde=len(res2)
print(f'Qtde: {qtde} elementos')

#Imprmir cada elemento
for t in res2:
    print(t)