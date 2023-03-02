
'''
Trabalhando com JSON PARTE 3
'''

import json

jogador_j = '{"nome": "Bruno","time": "aviadores","vivo": "True","energia": 100,"mochila": ["faca","corda", "linha", "arame"],"aeronaves": [{"tipo": "transporte", "habilidade": 80},{"tipo": "ataque","habilidade": 100},{"tipo": "reconhecimento", "habilidade": 100}]}'

jogador = json.loads(jogador_j)

#chaves
print('Imprimindo as chaves')
for c in jogador:
    print(c)
print('=============================')

#itens
print('Imprimindo as chaves')
for i in jogador.items():
    print(i)
print('=============================')

#valores
print('Imprimindo as valores')
for v in jogador.values():
    print(v)
print('=============================')

#nome do jogador
print('Imprimindo o nome do jogador')
print(jogador["nome"])
print('=============================')

#imprimir itens da mochila
print('Imprimindo os itens da mochila')
for im in jogador["mochila"]:
    print(im)
print('=============================')

#imprimir as aeronaves
print('Imprimindo as aeronaves')
for a in jogador["aeronaves"]:
    print(a)
print('=============================')


#imprimir os tipos de aeronaves
print('Imprimindo as aeronaves')
for a in jogador["aeronaves"]:
    print(a["tipo"])
print('=============================')

#imprimir o valor das habilidades de cada aeronaves
print('Imprimindo o valor das habilidades de cada aeronaves')
for a in jogador["aeronaves"]:
    print(a["habilidade"])
print('=============================')

#imprimindo as informacoes das aernovaves
print('Imprimindo as informacoes das aernovaves')
for a in jogador["aeronaves"]:
    print(f'{a["tipo"]} - {a["habilidade"]}')
print('=============================')