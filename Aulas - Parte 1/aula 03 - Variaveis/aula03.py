#Qualquer variável que criamos na parte de cima do programa, sao variaveis GLOBAIS, podem ser acessadas de qualquer parte do programa 
num1=num2=res=0


#criando uma função
def cn():
    #criando uma variavel dentro da função
    global canal #Quando declaramos uma variavel como GLOBAL, nao podemos inicializa-la na mesma linha
    canal = "CFB Cursos"
    print(canal)


#Chamando a função cn()
cn()

#Se tentarmos utilizar a variavel canal fora da função, o Python irá dar ERRO. Mas conseguimos acessar essa variavel se esta mesma variavel for definida dentro da funcao como GLOBAL
print(canal)


