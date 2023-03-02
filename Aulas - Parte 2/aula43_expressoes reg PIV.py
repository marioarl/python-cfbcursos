"""
Expressoes Regulares, RegEX sao como uma mini liguagem de programação e tem recursos bastante interessantes para trabalhar com STRINGS
PART IV
"""
#SUB - Substituira o caractere

import re  

texto = 'Curso de Python do CFB Cursos, canal do YouTube'

res = re.sub(" ", "-", texto)# 1o. parametro o que voce quer substituir / 2o parametro o novo caractere que substiuira o antigo / 3o parametro a variavel a ser feita a substituicao
print(res)
