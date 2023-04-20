#Criando conexao com o banco de dados SQLITE3

import sqlite3
from sqlite3 import Error

########## Criar CONEXAO
def ConexaoBanco():
    caminho="caminho do BD"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return con

vcon=ConexaoBanco()

######### Criar TABELA
vsql="""CREATE TABLE tb_contatos(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NONECONTATO TEXT(30),
            T_TELEFONECONTATO TEXT(14),
            T_EMAILCONTATO TEXT(30)
        );"""

def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada!")
    except Error as er:
        print(er)

criarTabela(vcon,vsql)        
vcon.close()