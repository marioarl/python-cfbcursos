# POO - HERANÇA - Quando temos uma classe que herda outra classe, criando a classe PAI e depois criando as classes FILHO que vão herdar a classe PAI.
class NPC: #Base, Pai, Super classe
    def __init__(self,nome,time,forca,municao):
        self.nome=nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 300
    def info(self):
        print(f'Nome....: {self.nome}')
        print(f'Time....: {self.time}')
        print(f'Força...: {self.forca}')
        print(f'Munição.: {self.municao}')
        print(f'Vivo....: {"Sim" if self.vivo else "Não"}')
        print(f'Energia.: {self.energia}')
        print('--------------------------------------')

class Soldado(NPC): #Herdando da classe NPC
    def __init__(self,nome,time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time,self.forca,self.municao) #Chamando o construtor da classe PAI

class Guarda(NPC):
    def __init__(self,nome,time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time,self.forca,self.municao) #Chamando o construtor da classe PAI

class Elite(NPC):
    def __init__(self,nome,time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time,self.forca,self.municao) #Chamando o construtor da classe PAI
    def inf(self):
        super().info()

s1 = Guarda('Olho vivo', 1)
s2 = Soldado('Bala na Agulha', 1)
s3 = Elite('Ninja', 1)
s4 = Guarda('Super Atento', 2)
s5 = Soldado('Tiro certo', 2)
s6 = Elite('Samurai', 2)

s1.vivo = False
s6.vivo = False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()