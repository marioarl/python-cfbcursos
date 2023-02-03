'''
O Loop FOR é utilizado para iterar uma sequencia(que pode ser uma lista, uma tupla, 
um dicionario, um conjunto ou sequencia)

a sintaxe é --> for x in carros, onde x é a variavel que armazenará o conteudo da lista, ou dicionario,

E o comando FOR irá imprimir cada um dos elementos da lista carros=[]
''' 

carros = ['HRV', 'Golf', "Argo", "Focus", 'Fit', 'Fusion', 'Polo']

for x in carros:
    print(x)
    if x == 'Golf':
        print('  VW')