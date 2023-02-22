
'''
Trabalhando com DATAS em Python e utilizando o strftime
'''

import datetime #Modulo que contem os metodos com datas


data = datetime.datetime.now() 
print(data) # imprimi data completa aaaa-mm-dd hh:mm:00.00000

print(data.day) #imprimir somente o dia
print(data.month) #imprimir somente o mes
print(data.year) #imprimi  somente o ano

nasc=datetime.datetime(1978,3,7)
print(nasc)# imprimi aaaa-mm-dd hh:mm:ss

#utilizando o strftime para mes, dia e ano
print(nasc.strftime('%a')) #imprimi o dia da semana abreviado(em ingles)
print(nasc.strftime('%A')) #imprimi o dia da semana completo (em ingles)
print(nasc.strftime('%w')) #imprimi o numero do dia da semana (0-domingo,1-segunda, 2 -terça...)
print(nasc.strftime('%d')) #imprimi o dia do mes
print(nasc.strftime('%b')) #imprimi o mes abreviado (ingles)
print(nasc.strftime('%B')) #imprimi o mes abreviado(em ingles)
print(nasc.strftime('%m')) #imprimi o numero do mes
print(nasc.strftime('%y')) #imprimi o ano com 2 digitos
print(nasc.strftime('%Y')) #imprimi o ano com 4 digitos
print(nasc.strftime('%j')) #imprimi o dia do ano (001 - 366)
print(nasc.strftime('%W')) #imprimi o numero da semana do ano 

#utilizando o strftime para horas
print(nasc.strftime('%H')) #imprimi a hora com 2 digits 00-23
print(nasc.strftime('%I')) #imprimi a hora com 2 digits 00-12
print(nasc.strftime('%p')) #imprimi se a hora é AM ou PM
print(nasc.strftime('%M')) #imprimi os MINUTOS
print(nasc.strftime('%S')) #imprimi os SEGUNDOS
print(nasc.strftime('%f')) #imprimi os MICROSEGUNDOS



