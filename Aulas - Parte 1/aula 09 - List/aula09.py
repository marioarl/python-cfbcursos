carros = ["HRV", "Golf", "Argo", "Focus"]

print(carros) #Imprimii a lista carros
print(carros[0]) #Imprimir o indice 0 da lista carros
print(carros[-1]) #Quando colocamos indice negativo agora é da direita para a esquerda, onde -1 é o 1o. indice de tras para frente

#Alterando a lista com indice 3
carros[3] = "Fusion"
print(carros)

#Incluindo itens na lista
carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")
print(carros)

#Tamanho da lista
print(len(carros), " carros na lista")

#Remover itens da lista
carros.remove("Fusion")
print(carros)
print(len(carros), " carros na lista")

#Remover com o metodo pop(), remove o utlimo elemento da lista
carros.pop()
print(carros)
print(len(carros), " carros na lista")

#remover com o metodo del, que remove o item de acordo com o indice informado
del carros[2]
print(carros)
print(len(carros), " carros na lista")

#Copiar uma lista em outra lista
carros2 = carros
print(carros2)
print(len(carros2), " carros na lista")

#Fundir um lista em outra e gerando um nova lista
carros3 = ["Fusca", "147", "Brasilia", "Celta"]

carros4 = carros2 + carros3
print(carros4)
print(len(carros4), " carros na lista")
