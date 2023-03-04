# Criando um dicionario com valores, mas é possivel cria-lo vazio ( carro = {} ou carro = dict())
carro = {'Fabricante': 'Honda', 'Modelo': 'HRV', 'Ano': '2016', 'Cor': 'Vermelho' }

#for x in carro:
    #print(x) # somente as chaves (Fabricante, modelo, ano e cor)
    #print(carro[x]) # somente os valores (Honda, HRV, 2016, Prata)

for k in carro.keys(): # O metodo keys() do dicionario carro, tambem imprimi as chaves
    print(k)


for v in carro.values(): # O metodo values() do dicionario carro, tambem imprimi os valores
    print(v)

for k, i in carro.items(): # O metodo items() do dicionario carro, tambem imprimi os valores e as chaves
    print(f'{k}: {i}') 

#Para saber se temos uma chave chamada Modelo
if "Modelo" in carro:
    print('SIM, modelo é uma chave')

#retornar o tamamnho do Dicionario
print(f'Tamanho do dicionario {len(carro)}')

#adicionar item no dicionario
carro['Cambio'] = "Automatico"
print(carro)

#remover item do dicionario
carro.pop("Cambio") # ou del carro["Cambio"]
print(carro)

#limpar todo o dicionario
carro.clear()

#Dicionario dentro de dicionario
carros = {
    "Carro1": {
    "Fabricante": "Honda",
    "Modelo": "HRV"
    },
    "Carro2": {
    "Fabricante": "Volkswagen",
    "Modelo": "Golf"
    },
    "Carro3": {
    "Fabricante": "Ford",
    "Modelo" : "Focus"
    }
}
print(carros)
print(carros["Carro1"]["Fabricante"])
