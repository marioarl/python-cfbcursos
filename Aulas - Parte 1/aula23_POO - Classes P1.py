# POO - Classe é a especificacao de um objeto que é uma instancia da classe

#criando uma classe
class Carro:
    velMax = 0
    ligado=False
    cor=""

#Instanciando o objeto
c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.velMax=200
c1.cor="Preto"
c1.ligado=False

print(f'velocidade Maxima: {c1.velMax}Km/h')
print(f'Cor: {c1.cor}')
estado = 'SIM' if c1.ligado else "NÃO"
print(f'Ligado: {estado}')
