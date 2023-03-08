from os import system
from colorama import Fore, init
init(autoreset=True)
carros = []

class Carro:
    nome = ""
    pot=0
    velMax=0
    ligado=False
    def __init__(self, nome, pot): #Construtor
        self.nome=nome
        self.pot=pot
        self.velMax=pot*2
        self.ligado=False
    
    def ligar(self):
        self.ligado=True
    
    def desligar(self):
        self.ligado=False

    def info(self):
        print(f'Nome...........:{self.nome} ')
        print(f'Potencia.......:{self.pot} ')
        print(f'Vel. Máxima....:{self.velMax} ')
        print(f'Ligado.........:{"Sim" if self.ligado else "Não"}')

def Menu(): #Funcao para desenhar o menu
    system('cls') or None
    print('1 - Novo Carro')
    print('2 - Informações do carro')
    print('3 - Excluir Carro')
    print('4 - Ligar o Carro')
    print('5 - DesLigar o Carro')
    print('6 - Listar os Carro')
    print('7 - Sair')
    print(f'Quantidade de carros: {len(carros)} ')
    opc = int(input('Digite uma opção: '))
    return opc

def NovoCarro():
    system('cls') or None
    n = str(input('Nome do Carro.....: ')).strip()
    p=int(input('Potencia do Carro...: '))
    car=Carro(n,p)
    carros.append(car)
    print('Novo carro criado')
    system('pause')

def informacoes():
    system('cls')
    n=int(input('Numero do carro que deseja ver as informações...: '))
    try:
        carros[n].info()
    except:
        print('CARRO NÃO EXISTE NA LISTA')
    system('pause')

def excluirCarro():
    system('cls')
    n=int(input('Numero do carro que deseja excluir...: '))
    try:
        del carros[n]
    except:
        print('CARRO NÃO EXISTE NA LISTA')
    system('pause')

def LigarCarro():
    system('cls')
    n=int(input('Numero do carro que deseja ligar...: '))
    try:
        carros[n].ligar()
        print('Carro ligado')
    except:
        print('CARRO NÃO EXISTE NA LISTA')
    system('pause')

def DesligarCarro():
    system('cls')
    n=int(input('Numero do carro que deseja desligar...: '))
    try:
        carros[n].desligar()
        print('Carro desligado')
    except:
        print('CARRO NÃO EXISTE NA LISTA')
    system('pause')

def ListarCarros():
    system('cls')
    p=0
    for c in carros:
        print(f'{p} - {c.nome}')
        p +=1
    system('pause')