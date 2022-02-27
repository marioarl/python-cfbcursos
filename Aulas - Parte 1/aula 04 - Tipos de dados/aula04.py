

x = 1 #Definindo a variavel x como INT
print("Valor: ", x)
print("Tipo: ", type(x)) #Imprimindo o tipo de dados da variavel x
print("_______________")

y = "CFB Cursos" #Definindo a variavel y como STRING
print("Valor: ", y)
print("Tipo: ", type(y)) 
print("_______________")

z = 15.6 #Definindo a variavel z como FLOAT
print("Valor: ", z)
print("Tipo: ", type(z)) 
print("_______________")

a = False #Definindo a variavel a como BOOLEAN
print("Valor: ", a)
print("Tipo: ", type(a))
print("_______________")

n1=5
n2=2
b = complex(n1,n2) #Definindo a variavel b como COMPLEX, onde temos a parte REAL e a IMAGINARIA
print(b.real)
print(b.imag)
print("Tipo: ", type(b))
print("_______________")


x = ["Carro", "Aviao", "Navio", 1, 1.18, True] #Criando uma lista (LIST / ARRAY), podemos colocar tipos diferentes dentro da LIST
print("Valor: ", x[0])
print("Tipo: ", type(x))
print("_______________")

x1 = ("Carro", "Aviao", "Navio", 1, 1.18, True) #Criando uma TUPLA (TUPLE), podemos colocar tipos diferentes dentro da LIST e ela nao pode ser alterada
print("Valor: ", x1[0])
print("Tipo: ", type(x1))
print("_______________")

x2 = {  #Criando um DICIONARIO (DICTONARY), chave : valor
    "canal" : "CFB Cursos",
    "Curso" : "Curso de Python",
    "Nome" : "Mario"
}
print("Valor: ", x2["canal"])
print("Tipo: ", type(x2))
print("_______________")

x3 = {5,7,4,5,7,4,8} #Criando um SET , mesmo que repetindo valores na criacao da variavel, ele nao repete quando imprimi
print("Valor: ", x3)
print("Tipo: ", type(x3))
print("_______________")



