'''Modulo externos / Funcoes em arquivos externos
Modulo é simplesmente um arquivo contendo ódigos Python que podem ser utilizados
por outros programas.

Um modulo completo pode ser chamado por outros programas atraves da declaracao IMPORT.
Mas só podemos importar modulos para um programa se eles estiverem dentro do mesmo diretorio,
ou se estiver em uma lista de diretorios dadas pela varave sys.path.

Neste caso dentro do diretorio aula34, foi criado 2 arquivos (aula34.py e canal.py)
o canal.py é um arquivo onde está uma funcao chamada canal() que será utilizado pelo
programa do arquivo aula34.py
'''
import canal as cn # importando canal como ALIAS

cn.canal_nome()
print(cn.jogador['nome'])

#verificando tudo que está disponivel no modulo canal
res = dir(cn)
print(res)