import random

num_i = 10
num_f = 5.2
num_c = 1j

x = int(num_f)
y = float(num_i)

print("Valor: " + str(num_i) + " - Tipo: " + str(type(num_i)))
print("Valor: " + str(num_f) + " - Tipo: " + str(type(num_f)))
print("Valor: " + str(num_c) + " - Tipo: " + str(type(num_c)))

print("Valor: " + str(x) + " - Tipo: " + str(type(x)))
print("Valor: " + str(y) + " - Tipo: " + str(type(y)))

num_r= random.randrange(0,59) #Gerar um numero aleatorio entre 0 e 59
print("Valor: " + str(num_r) + " - Tipo: " + str(type(num_r)))

num_r2 = [ #Gerando 6 numeros aleatorios entre 0 e 59 e colocando na LISTA
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
]
print("Valor 1: " + str(num_r2[0]))
print("Valor 2: " + str(num_r2[1]))
print("Valor 3: " + str(num_r2[2]))
print("Valor 4: " + str(num_r2[3]))
print("Valor 5: " + str(num_r2[4]))
print("Valor 6: " + str(num_r2[5]))

