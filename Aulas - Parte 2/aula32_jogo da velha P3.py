from os import system
import random
from colorama import Fore,Back, Style

#VARIAVEIS
jogarNovamente = 's'
jogadas=0
quemJoga=2 #2 - Jogador  1-CPU
maxJogadas=9
vit='n'
velha=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

#FUNCOES
#gerenciamento da tela
def tela():
    global velha
    global jogadas
    system('cls')
    print('    0   1   2')
    print(f'0:  {velha[0][0]} | {velha[0][1]} | {velha[0][2]}')
    print('   -----------')
    print(f'1:  {velha[1][0]} | {velha[1][1]} | {velha[1][2]}')
    print('   -----------')
    print(f'2:  {velha[2][0]} | {velha[2][1]} | {velha[2][2]}')
    print(f'Jogadas: {Fore.GREEN}{jogadas}{Fore.RESET}')

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input('Linha..: '))
            c = int(input('Coluna.: '))
            while velha[l][c] != " ":
                l = int(input('Linha..: '))
                c = int(input('Coluna.: '))
            velha[l][c] = 'X'
            quemJoga=1
            jogadas += 1
        except:
            print('Jogada inválida')
            system('pause')
            #vit='n'
def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha[l][c] != " ":
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        velha[l][c]='O'
        jogadas += 1
        quemJoga = 2

def verificarVitoria():
    global velha
    vitoria = 'n'
    simbolos= ['X', 'O']
    for s in simbolos:
        vitoria = 'n'
        #Verificar Linhas
        il= ic =0 #il = indice de linhas, ic=indice de coluna
        while il < 3:
            soma=0
            ic=0
            while ic < 3:
                if velha[il][ic] == s:
                    soma += 1
                ic += 1
            if soma == 3:
                vitoria=s
                break
            il+=1
        if vitoria != 'n':
            break
        #Verificar olunas
        while ic < 3:
            soma=0
            il=0
            while il < 3:
                if velha[il][ic] == s:
                    soma += 1
                il += 1
            if soma == 3:
                vitoria=s
                break
            ic += 1
        if vitoria != 'n':
            break
        #Verificar diagonal 1
        soma = 0
        idiag = 0
        while idiag < 3:
            if velha[idiag][idiag] == s:
                soma += 1
            idiag += 1
        if soma == 3:
            vitoria=s
            break

        #Verificar diagonal 2
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc < 3:
            if velha[idiagl][idiagc] == s:
                soma += 1
            idiagl += 1
            idiagc -= 1
        if soma == 3:
            vitoria=s
            break
    return vitoria
        


#LOOP PRINCIPAL
while True:
    tela()
    jogadorJoga()
    cpuJoga()

# O programa não está completo