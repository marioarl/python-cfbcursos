'''
A estrutura de repetição WHILE é usada para execução repetida, desde que a
expressão (teste loógico) seja verdadeira
'''

i = 0 # inicializa a variavel i com zero
while i <10: # Enquanto a variavel i for menor que 10, irá imprimir o i na tela
    print(i)
    i+=1 # Iteração da variavel i, para que o programa não caia em loop infinito
print('Fim do loop')


'''
Abaixo podemos utilizar tambem o comando break para que o loop seja parado, mesmo
que o teste logico esteja como FALSE
'''
j = 0 
while j <10: 
    print(j)
    j+=1
    if j <=5:
        break
print('Fim do loop')

'''
Pode-se tambem utilizar o WHILE para varrer uma lista, tupla ou dicionario
'''

carros = ['HRV', 'Golf', 'Argo', 'Onix', 'Focus']
k = 0
tam = len(carros) # A variavel tam está lendo o tamanho da lista carros
while k<tam: # e o loop irá parar quando o k for menor que a variavel tam
    print(carros[1])
    k+=1
print('\nFim do loop')


'''
Utilizando um FLAG para parar o LOOP while
'''
carros2 = []
carro= str(input('Digite o nome do novo carro: '))
while carro != "-1": # o loop irá parar quando o usuario digitar -1 no teclado
    carros.append(carro)
    carro=input('Digite o nome do novo carro: ')
print(carros)