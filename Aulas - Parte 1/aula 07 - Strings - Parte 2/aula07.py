


texto = "Curso de Python"
palavra = "Python"
res = palavra in texto #Retorna True ou False, o operador in é CASE SENSITIVE
print(res)

res2 = palavra not in texto #Retorna True ou False, o not in é CASE SENSITIVE
print(res2)

#Concatenar strings
curso = "Curso de Python"
canal = "CFB Cursos"

res3 = curso + " do canal " + canal
print(res3)

cidade = "Sao Paulo"
dia = 3
mes = "Março"
ano = 2019


print(cidade + ", " + str(dia) + " de " + mes + " de " + str(ano)) #Executar o casting das variaveis int

#utilizando o format
data = "{}, {} de {} de {}"
print(data.format(cidade,dia,mes,ano))

#Caracteres de escape
#\n - Quebra a linha
#\t - Tabulacao
#\" - Imprimir aspas duplas
#\' - Imprimir aspas simles
#\b - Backspace

