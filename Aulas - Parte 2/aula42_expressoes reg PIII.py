"""
Expressoes Regulares, RegEX sao como uma mini liguagem de programação e tem recursos bastante interessantes para trabalhar com STRINGS
PART III
"""
#SPLIT - Encontrara a divisão dos caracteres, onde foi encontrado um espaço por exemplo, retornando uma lista

import re  

texto = 'Curso de Python do CFB Cursos, canal do YouTube'

res = re.split(" ", texto)# 1o. parametro o que voce quer encontrar a divisao / 2o parametro o lugar a ser pesquisado
print(res)
print(res[2])

#imprimir todos os elementos
for t in res:
    print(t)
