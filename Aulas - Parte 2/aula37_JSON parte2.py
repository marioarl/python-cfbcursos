
'''
Trabalhando com JSON PARTE 2
'''

import json

#Dicionario - Quando temos um DICIONARIO em Python e convertemos para JSON, o mesmo vira um objeto JSON
carros_dictionary={
    'marca':'honda',
    'modelo': 'HRV',
    'cor': 'vermelho'
}

#lista - Quando temos uma LISTA em Python e convertemos para JSON, o mesmo vira um array JSON
carros_list=['honda', 'volkswagem', 'ford', 'fiat','chevrolet']

#tupla - Quando temos uma TUPLA em Python e convertemos para JSON, o mesmo vira um array JSON
carros_tupla=('honda', 'volkswagem', 'ford', 'fiat', 'chevrolet')

#Convertendo o dict() em JSON
print('Convertendo o dict() em JSON')
carros_j = json.dumps(carros_dictionary)
print(carros_j)
print('='*50)

#Convertendo o list() em JSON
print('Convertendo o list() em JSON')
carros_j1 = json.dumps(carros_list)
print(carros_j1)
print('='*50)

#Convertendo o ltuple() em JSON - Neste caso a tupla vira um array [] e não como ()
print('Convertendo o tuple() em JSON')
carros_j2 = json.dumps(carros_tupla)
print(carros_j2)
print('='*50)


#FORMATANDO A SAIDA DO METODO DUMPS(PARAMETROS)

#ident - Faz uma identação à esquerda com a quantidade desejada
carros_j = json.dumps(carros_dictionary, indent=4)
print(carros_j)
print('='*50)

#separators - Troca o : que separam os campos por outro separador que deseja
carros_j = json.dumps(carros_dictionary, indent=4, separators=(":", "=")) 
print(carros_j)
print('='*50)

#sort_keys - Imprimirá ordenando as chaves (True ou False)
carros_j = json.dumps(carros_dictionary, indent=4, separators=(":", "="), sort_keys=True) 
print(carros_j)
print('='*50)

