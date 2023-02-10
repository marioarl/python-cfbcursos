# Funcoes Lambda ou anonimas

#em uma variavel(soma) + palavra chave (lambda) + argumentos de entrada(a e b) : expressao 
soma = lambda a,b: a + b

print(soma(2,5))

#mais uma funcao lambida com mais de 2 argumentos
mult = lambda a,b,c:(a+b)*c
print(mult(2,5,3))

#criando uma funcao lambda sem associar a variavel
print((lambda a,b: a+b)(3,2))