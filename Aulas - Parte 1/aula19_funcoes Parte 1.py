n1 = 15
n2 = 7

def somar():
    r = n1 + n2
    print('Soma de ' + str(n1) + ' e ' + str(n2) + ' = ' + str(r))

def subtrair():
    r = n1 - n2
    print('Subtração de ' + str(n1) + ' e ' + str(n2) + ' = ' + str(r))

def multiplicar():
    r = n1 * n2
    print('Multiplicação de ' + str(n1) + ' e ' + str(n2) + ' = ' + str(r))

#Criando uma funcao chamando outras duas funcoes
def calculos():
    somar()
    subtrair()
    multiplicar()
        
#somar()
#subtrair()
calculos()