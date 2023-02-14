# Iterators - Objeto que pode ser iterado

carros = ['HRV', 'Polo', 'Jetta', 'Cruze', 'Fusion']

#utilizando FOR
for c in carros:
    print(c)
print('-'*30)
#Utilizando iterator
itCarros = iter(carros)
print(next(itCarros)) # Cada vez que chamarmos o next() imprimira o proximo carro
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
#print(next(itCarros)) # Se tentar imprimir mais do que conta na lista carros, irá gerar uma excecao StopIteration

#utilizando o iterator dentro de um While
while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print('Fim da lista')
        break
