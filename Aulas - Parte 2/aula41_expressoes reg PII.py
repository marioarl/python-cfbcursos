"""
Expressoes Regulares, RegEX sao como uma mini liguagem de programação e tem recursos bastante interessantes para trabalhar com STRINGS
PART II
"""
#SEARCH - 

import re #Importando a biblioteca REGEX, que irá retornar a posição inicial ou final da primeira ocorrencia que encontrar 

texto = 'Curso de Python do CFB Cursos, canal do YouTube'

res = re.search("canal", texto)# 1o. parametro o que voce quer pesquisar / 2o parametro o lugar a ser pesquisado

if res != None:
    print(f'Começa no indice {res.start()}') #Indicando onde a pesquisa deve ser feita (start ou end)
    print(f'Termina no indice {res.end()}') # Aqui mostrará o indice de onde a palavra Curso termina.
    pi = res.start()
    pf = res.end()
    tam = pf - pi
    print(f'O tamanho da string é {tam}')
else:
    print('Não encontrado')

