
'''
Trabalhando com JSON
'''

import json

carros_json= '{"marca": "honda", "modelo":"HRV", "cor": "prata"}'

#variavel que carregará o json

carros=json.loads(carros_json)

print(carros)
print(carros['marca'])
print(carros['modelo'])
print('='*30)
for x in carros.values():
    print(x)
print('='*30)
for x in carros.items():
    print(x)
print('='*30)
for x in carros.keys():
    print(x)
print('='*30)

for k,v in carros.items():
    print(k,v)
print('='*30)

#Converter o dict() em json

carros2 = {"marca": "honda", "modelo":"HRV", "cor": "prata"}

carros2_json = json.dumps(carros2)

print(carros2_json)