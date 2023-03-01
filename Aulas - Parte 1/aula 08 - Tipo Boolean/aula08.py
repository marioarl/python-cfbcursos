aula = 10 < 15 #Variável tipo Bool pode ser definida com True ou False, ou uma expressao que retorne True ou False

texto = "CFB Cursos"
texto2 = ""
print(aula)

#Converter string em bool com casting
print(bool(texto))

#Strings vazias retornam False
print(bool(texto2))

#Com uma condicao IF
if texto2:
    print("Possui texto")
else:
    print("Vazio")

#Variavel numerica, qualquer valor diferente de 0 é considerado True e 0 retorna False
n1 = 100
print(bool(n1))
n2 = 0
print(bool(n2))

#Em uma lista, dict, tupla
lista = [1,2,3]
lista2 = ()
dicionario = {}
print(bool(lista))
print(bool(lista2))
print(bool(dicionario))