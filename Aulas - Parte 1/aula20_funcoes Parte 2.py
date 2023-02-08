# Funcoes com parametros

def somar(n1,n2): #Parametros n1 e n2
    r = n1 + n2
    print('Soam de ' + str(n1) + ' e ' + str(n2) + ' = ' + str(r))

somar(5,7)
somar(12,8)
somar(1,2)

# Argumentos arbritários
def textos(*txt): 
    for t in txt: #imprimindo todos os elementos
        print(t)


textos  ('CFB Cursos', 'Python', 'Canal', 'Curso', 'Computador')

#Funcao somar com argumentos arbritarios
def somar2(*num):
    r = 0
    for n in num:
        r += n

    print('Soma = ' + str(r))

somar2(3,6,7)
somar2(5,6)
somar2(10,67,45,90,102)

#Argumentos com valores padroes
def carros(c = 'Golf'): 
    print('Modelo: ' + c)

#Se passarmos um valor para o parametro da funcao ela irá imprimir
carros('HRV')

#Mas se não passarmos, a funcao irá imprimir o valor padrao 'Golf'
carros()

#Utilizando uma lista como valor para a funcao
valores = [1,5,3,2]

def somar3(lista):
    r = 0
    for n in lista:
        r += n

    print('Soma = ' + str(r))

somar3(valores) # Irá imprimir a soma de todos os numeros da lista valores