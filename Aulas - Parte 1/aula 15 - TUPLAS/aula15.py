'''
TUPLAS são usadas para armazenar itens em uma unica variavel.

TUPLA é um dos 4 tipos de dados built-in em Python para armazenar coleçoes 
de dados, onde temos tambem as listas, os sets e os dicionarios, todos com 
diferentes qualidade de uso.

Uma TUPLA é imutavel, ou seja, não é possivel altera-la depois que o programa
estiver em uso.
'''

carros1 = ('HRV', 'Golf', 'Argo') #A TUPLA pode ser criada desta forma
carros2 = 'HRV', 'Golf', 'Argo'# Pode ser criada tambem sem a necessidade de utilizr os parenteses
carros3 = tuple() # Neste caso tambem pode-se criar a TUPLA vazia
print(carros1)
print(carros2)
print(carros3)

'''
Pode-se tambem criar uma TUPLA e vincular em uma LISTA
'''
t_carros=('HRV', 'Golf', "Argo")
l_carros=list(t_carros)
l_carros[2]= 'Focus'
t_carros=tuple(l_carros)

for x in t_carros:
    print(x)