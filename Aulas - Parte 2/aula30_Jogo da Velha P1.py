from os import system
import random
from colorama import Fore,Back, Style

#VARIAVEIS
jogarNovamente = 's'
jogadas=0
quemJoga=2 #2 - Jogar  1-CPU
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

tela()