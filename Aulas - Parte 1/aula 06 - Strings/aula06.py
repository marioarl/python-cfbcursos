curso = "Curso de Python" #STring nada mais é do que um Array de caracteres


print(curso)
print(curso[2]) #Posicao de indice 2 vai imprimir a letra r
print(curso[9]) #Posicao de indice 2 vai imprimir a letra P
print(curso[0:5]) #Faixa de intervalo vai imprmir Curso
print(curso[9:15]) #Faixa de intervalo vai imprmir Python

print("Tamanho: " + str(len(curso)))#Retorna o tamanho da string

print(curso.strip())#Strip retira os espacos no inicio e no fim da string

print(curso.lower().strip())#Lower deixa a string toda em minusculo. E podemos utilizar tambem a funcao strip() junto

print(curso.upper().strip())#upper deixa a string toda em maisculo.

print(curso.replace("Python", "C#"))#replace() troca um caracter ou uma string por outro caracter ou string

a=curso.split(" ")#split vai separar o conteudo da string, neste caso quando houver um espaco e vai armazenar na variavel a 
print(a[0]) #imprimindo a variavel a no indice 0 (Curso)
print(a[1])
print(a[2])

