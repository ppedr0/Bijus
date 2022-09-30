from ast import Delete
from http import client
from msilib.schema import Error
from PyQt5 import uic, QtWidgets # Import do Pyqt5
import mysql
import mysql.connector


connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '202173',
        database = 'biju'
    )

# |=-----------------------------------------------------------------VERIFICA_SENHA_FUNC--------------------------------------------------------------------------=| #

def verifica_senha_func():
    
    global user
    
    user = func_login.nome.text()

    senha_v = func_login.senha.text()


    cursor = connect.cursor()

    cursor.execute(" select nome, senha from cd_func where nome = '{}' and senha = '{}'". format(user, senha_v))

    for (nome, senha) in cursor:
        if user == nome or senha_v == senha:
            chama_opçoes()
            func_login.nome.setText('')
            func_login.senha.setText('')
        elif user   != nome or senha_v != senha:
            func_login.nome.setText('|Nome ou senha INVALIDOS|')

# |=-----------------------------------------------------------------FUNÇÃO PARA VERIFICAR USUARIO E SENHA--------------------------------------------------------------------------=| #

def verifica_senha_user():
    
    global login

    
    
    login = user_login.nome.text()

    senha_v = user_login.senha.text()

    catalogo.nome.setText(login)



    cursor = connect.cursor()

    cursor.execute(" select nome, senha from cd_user where nome = '{}' and senha = '{}'". format(login, senha_v))

    for (nome, senha) in cursor:
        if login == nome or senha_v == senha:
            chama_catalogo()
            user_login.nome.setText('')
            user_login.senha.setText('')
        elif login != nome or senha_v != senha:
            user_login.nome.setText('|Nome ou senha INVALIDOS|')

# |=------------------------------------------------------------FUNÇAO PARA CADASTRODE CLIENTE-------------------------------------------------------------------------------=| #

def cadastro_cliente():

    linha1 = cd_user.nome.text()

    linha2 = cd_user.senha.text()

    linha3 = cd_user.nasc.text()

    linha4 = cd_user.cpf.text()

    linha5 = cd_user.cep.text()

    linha6 = cd_user.endereco.text()

    linha7 = cd_user.telefone.text()

    linha8 = cd_user.email.text()


    inserir = "INSERT INTO cd_user (id ,nome ,senha , nasc ,cpf ,cep ,endereco ,telefone ,email) values (null, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    dados = (linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8)

    cursor = connect.cursor()

    cursor.execute(inserir, dados)
  
    connect.commit()

    cursor.close()

# |=------------------------------------------------------------FUNÇAO PARA CADASTRODE FUNCIONARIO-------------------------------------------------------------------------------=| #

def cadastro_func():

    linha1 = cd_func.nome.text()

    linha2 = cd_func.email.text()

    linha3 = cd_func.senha.text()

    linha4 = cd_func.cep.text()

    linha5 = cd_func.telefone.text()

    linha6 = cd_func.endereco.text()

    linha7 = cd_func.nasc.text()

    linha8 = cd_func.cpf.text()


    inserir = "INSERT INTO cd_func (id ,nome ,senha , nasc ,cpf ,cep ,endereco ,telefone ,email) values (null, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    dados = (linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8)

    cursor = connect.cursor()

    cursor.execute(inserir, dados)
  
    connect.commit()

    cursor.close()

# |=---------------------------------------------------------------FUNÇÃO PARA CADASTRO DE FORNECEDOR----------------------------------------------------------------------------=| #

def cadastro_forn():
    
    linha1 = cd_fornecedor.id.text()

    linha2 = cd_fornecedor.nome.text()

    linha3 = cd_fornecedor.id_prod.text()

    linha4 = cd_fornecedor.marca.text()

    linha5 = cd_fornecedor.produto.text()

    linha6 = cd_fornecedor.quantidade.text()

    linha7 = cd_fornecedor.telefone.text()

    linha8 = cd_fornecedor.email.text()

    inserir = "INSERT INTO cd_fornecedor (id, nome, cd_produto, marca, produto, quantidade, telefone, email) values (%s , %s, %s, %s, %s, %s, %s, %s)"
    
    dados = ( linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8)

    cursor = connect.cursor()

    cursor.execute(inserir, dados)

    connect.commit()

    cursor.close()

    chama_opçoes()


# |=----------------------------------------------------------FUNÇÂO PARA CADASTRO DE PRODUTO---------------------------------------------------------------------------------=| #

def cadastro_prod():
    
    linha1 = cd_prod.nome.text()

    linha2 = cd_prod.preco.text()

    linha3 = cd_prod.tipo.text()

    linha4 = cd_prod.marca.text()

    linha5 = cd_prod.tamanho.text()

    linha6 = cd_prod.preco_comp.text()

    inserir = "INSERT INTO cd_prod (id, nome, descricao, marca, tamanho,preco,preco_compra ) values (null, %s, %s, %s, %s, %s, %s)"
    
    dados = (linha1, linha2, linha3, linha4, linha5, linha6)

    cursor = connect.cursor()

    cursor.execute(inserir, dados)

    connect.commit()

    cursor.close()

# |=----------------------------------------------------------FUNÇÃO PARA ALTERAR DADOS DO CLIENTE---------------------------------------------------------------------------------=| #

def alteracao(): 

    consulta_sql= "SELECT * FROM biju.cd_user where nome= '{}'".format(login)
    cursor = connect.cursor()
    cursor.execute(consulta_sql)
    linhas= cursor.fetchall() 

    for linha in linhas:
        
        alt_dados.show()
        tela_user.hide()

        id = alt_dados.id.setText(linha[0])
        alt_dados.nome.setText(linha[1])
        alt_dados.senha.setText(linha[2])
        alt_dados.cpf.setText(linha[3])
        alt_dados.dt_nasc.setText(linha[4])
        alt_dados.endereco.setText(linha[5])
        alt_dados.cep.setText(linha[6])
        alt_dados.telefone.setText(linha[7])
        alt_dados.email.setText(linha[8])
        
        alt_dados.atualizar.clicked.connect(sv_dados)

def sv_dados():
    linha0 = alt_dados.id.text()

    linha1 = alt_dados.nome.text()

    linha2 = alt_dados.senha.text()

    linha3 = alt_dados.dt_nasc.text()

    linha4 = alt_dados.cpf.text()

    linha5 = alt_dados.cep.text()

    linha6 = alt_dados.endereco.text()

    linha7 = alt_dados.telefone.text()

    linha8 = alt_dados.email.text()

    salvar = connect.cursor()

    update= "update cd_user set nome = '{}', senha = '{}', nasc = '{}', cpf = '{}', cep = '{}', endereco = '{}', telefone = '{}', email = '{}' where id = '{}'".format(linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha0)

    salvar.execute(update)

    connect.commit()

    volta_dados()

# |=----------------------------------------------------------FUNÇÃO PARA EXCLUIR DADOS DO CLIENTE -------------------------------------------------------------------------------=| #

def excluir(): 

    consulta_sql= "SELECT * FROM biju.cd_user where nome= '{}'".format(login)
    cursor = connect.cursor()
    cursor.execute(consulta_sql)
    linhas= cursor.fetchall() 

    for linha in linhas:
        
        tela_user.hide()
        deletar.show()

        deletar.id.setText(linha[0])
        deletar.nome.setText(linha[1])
        deletar.senha.setText(linha[2])
        deletar.cpf.setText(linha[3])
        deletar.nasc.setText(linha[4])
        deletar.endereco.setText(linha[5])
        deletar.cep.setText(linha[6])
        deletar.telefone.setText(linha[7])
        deletar.email.setText(linha[8])

def confi_excluir():

    salvar = connect.cursor()

    update= "delete from cd_user where nome = '{}'".format(login)

    salvar.execute(update)

    connect.commit()
    deletar.hide()
    volta_dados()

# |=----------------------------------------------------------FUNÇÃO PARA EXCLUIR DADOS DO FORNECEDOR ------------------------------------------------------------------------=| #

def alteracao_func(): 

    consulta_sql= "SELECT * FROM biju.cd_func where nome= '{}'".format(user)
    cursor = connect.cursor()
    cursor.execute(consulta_sql)
    linhas= cursor.fetchall() 
    alt_dados.hide()
    
    for linha in linhas:
        
        alt_dados.show()
        tela_user.hide()

        id = alt_dados.id.setText(linha[0])
        alt_dados.nome.setText(linha[1])
        alt_dados.senha.setText(linha[2])
        alt_dados.cpf.setText(linha[3])
        alt_dados.dt_nasc.setText(linha[4])
        alt_dados.endereco.setText(linha[5])
        alt_dados.cep.setText(linha[6])
        alt_dados.telefone.setText(linha[7])
        alt_dados.email.setText(linha[8])
        
        alt_dados.atualizar.clicked.connect(sv_dados)

def sv_dados():
    linha0 = alt_dados.id.text()

    linha1 = alt_dados.nome.text()

    linha2 = alt_dados.senha.text()

    linha3 = alt_dados.dt_nasc.text()

    linha4 = alt_dados.cpf.text()

    linha5 = alt_dados.cep.text()

    linha6 = alt_dados.endereco.text()

    linha7 = alt_dados.telefone.text()

    linha8 = alt_dados.email.text()

    salvar = connect.cursor()

    update= "update cd_user set nome = '{}', senha = '{}', nasc = '{}', cpf = '{}', cep = '{}', endereco = '{}', telefone = '{}', email = '{}' where id = '{}'".format(linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha0)

    salvar.execute(update)

    connect.commit()

    volta_dados()

# |=----------------------------------------------------------FUNÇÃO PARA EXCLUIR DADOS DO FORNECEDOR ------------------------------------------------------------------------=| #

def bt_pesquisar():
    global psq
    
    cd_opções.hide()
    cd_func.show()

    psq= cd_func.nome.text()
  


def alteracao_func(): 

    consulta_sql= "SELECT * FROM biju.cd_func where nome= '{}'".format(psq)
    cursor = connect.cursor()
    cursor.execute(consulta_sql)
    linhas= cursor.fetchall() 

    for linha in linhas:
        cd_func.hide()
        cd_func.show()

        cd_func.id.setText(linha[0])
        cd_func.nome.setText(linha[1])
        cd_func.senha.setText(linha[2])
        cd_func.cpf.setText(linha[3])
        cd_func.nasc.setText(linha[4])
        cd_func.endereco.setText(linha[5])
        cd_func.cep.setText(linha[6])
        cd_func.telefone.setText(linha[7])
        cd_func.email.setText(linha[8])
        
        cd_func.alterar.clicked.connect(func_dados)

def func_dados():
    
    linha0 = alt_dados.id.text()

    linha1 = alt_dados.nome.text()

    linha2 = alt_dados.senha.text()

    linha3 = alt_dados.dt_nasc.text()

    linha4 = alt_dados.cpf.text()

    linha5 = alt_dados.cep.text()

    linha6 = alt_dados.endereco.text()

    linha7 = alt_dados.telefone.text()

    linha8 = alt_dados.email.text()

    salvar = connect.cursor()

    update= "update cd_func set nome = '{}', senha = '{}', nasc = '{}', cpf = '{}', cep = '{}', endereco = '{}', telefone = '{}', email = '{}' where id = '{}'".format(linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha0)

    salvar.execute(update)

    connect.commit()

    chama_opçoes()

# |=------------------------------------------------------------FUNÇÕES DE CHAMAR TELAS---------------------------------------------------------------------------------------=| #

def delet():
    excluir()
    tela_user.hide()


def volta_dados():
    alt_dados.hide()
    deletar.hide()
    tela_user.show()

# Função para voltar tela cliente

def volta_cliente():
    alt_dados.hide()
    tela_user.show()

# Função para chamar login do cliente

def chama_L_user():
    user_login.show()
    pre_login.hide()
    
# Função para chamar tela de login do funcionario

def chama_L_func():
    func_login.show()
    pre_login.hide()

# Função para voltar a tela de opções

def volta_func_user():
    cd_user.hide()
    cd_func.hide()
    pre_login.show()
    func_login.hide()
    user_login.hide()

# Função para voltar tela de login do usuario

def chama_login():
    cd_user.hide()
    user_login.show()

# Função para chamar tela de cadastro do usuario

def cadastro_user():
    user_login.hide()
    cd_user.show()

# Função para  voltar a tela de login do usuario

def volta_cd_user():
    user_login.show()
    cd_user.hide()

# Função para função para voltartela de login do funcionario 

def volta_login():
    func_login.show()
    cd_opções.hide()

# Função para mostrar a tela de cadastro e esconder a tela de login

def chama_cadastro(): 
    cd_func.show()
    cd_opções.hide()
   
# Função para mostrar a tela de catalogo e esconder a tela de cadastro

def chama_catalogo():
    catalogo.show()
    user_login.hide()
    tela_user.hide()

# Função para mostrar a tela de escolha e esconder a tela de login

def chama_opçoes():
    cd_opções.show()
    func_login.hide()
    cd_func.hide()
    cd_prod.hide()
    cd_fornecedor.hide()
    cd_vendas.hide()
   
# Função para mostrar a tela de cadastro de vendas e esconder a tela de vendas

def chama_vendas():
    cd_vendas.show()
    cd_opções.hide()
   
# Função para mostrar a tela de cadastro de produto e esconder a tela de vendas

def chama_produtos():
    cd_prod.show()
    cd_opções.hide()

# Função para esconder a tela de escolha e mostrar a tela de login

def chama_cdvendas():
    cd_vendas.hide()
    cd_opções.show()

# Função para esconder a tela de cadastro de produtos e mostrar a tela de escolha

def volta_op_prod():
    cd_prod.hide()
    cd_opções.show()

# Função para esconder a tela de cadastro de venda e mostrar a tela de escolha

def volta_telaVendas_op():
    cd_vendas.hide()
    cd_opções.show()
   
# Função para mostrar a tela de pagamento e esconder a tela de catalogo

def tela_pagamento():
    pagamentos.show()
    catalogo.hide()

# Função para esconder a tela de pagamentos e mostrar a tela de  catalogo

def voltar_catalogo():
    pagamentos.hide()
    catalogo.show()
   
# Função para mostrar a tela de cadastro de fornecedor e esconder a tela de escolha

def chama_forne():
    cd_fornecedor.show()
    cd_opções.hide()

# Função para voltar tela opções _ fornecedores
 
def volta_forn():
    cd_opções.show()
    cd_fornecedor.hide()

# Função para esconder a tela de cadastro de cliente para a tela de vendas

def chama_cadastro_op():
    cd_func.show()
    cd_opções.hide()

# Função para chamar tela do usuario

def chama_user():
    tela_user.show()
    alt_dados.hide()
    catalogo.hide()

# Função desfazer login do usuario

def sair():
    tela_user.hide()
    pre_login.show()

# |=-------------------------------------------------------------------------------------------------------------------------------------------------------------------=| #

app=QtWidgets.QApplication([])

pre_login=uic.loadUi('pre_login.ui') # Inicializador antes da tela de login

user_login=uic.loadUi('login_user.ui') # Inicializador antes da tela de login do cliente

func_login=uic.loadUi('login_func.ui') # Inicializador da tela de login

tela_user=uic.loadUi('client (1).ui') # Inicializador da area do cliente

cd_user=uic.loadUi('cd_user.ui') # Inicalizador da tela de cadastro de usuario

cd_func=uic.loadUi('cd_func.ui') # Inicializador da tela de cadastro

catalogo=uic.loadUi('catalogo.ui') # Inicializador da tela de catálogo

cd_opções=uic.loadUi('cd_opções.ui') # Inicializador da tela de escolhas

cd_vendas=uic.loadUi('cd_vendas.ui') # Inicializador da tela de cadastro de vendas

cd_prod=uic.loadUi('cd_prod.ui') # Inicializador da tela de cadastro de produtos

cd_fornecedor=uic.loadUi('cd_fornecedor.ui') # Inicializador da tela de cadastro de fornecedor

pagamentos=uic.loadUi('pagamentos.ui') # Inicializador da tela de pagamento

alt_dados=uic.loadUi('alt_dados.ui') # Inicializador da tela de alteração de dados

deletar=uic.loadUi('delete.ui') # Inicializador para deletar dados do cliente 
 
# |=---------------------------------------------------------------PRE_LOGIN---------------------------------------------------------------------------------------------=| #

pre_login.cliente.clicked.connect(chama_L_user)
pre_login.funcionario.clicked.connect(chama_L_func)

# |=---------------------------------------------------------------LOGIN_FUNC--------------------------------------------------------------------------------------------=| #

func_login.entrar.clicked.connect(verifica_senha_func) # Botão de entrar da tela de login para tela de escolha
func_login.voltar.clicked.connect(volta_func_user) # Botão para voltar a tela de login

# |=---------------------------------------------------------------LOGIN_USER--------------------------------------------------------------------------------------------=| #

user_login.registrar.clicked.connect(cadastro_user) # Botão de entrar da tela de login
user_login.entrar.clicked.connect(verifica_senha_user) # Botão de entrar da tela de login para tela de escolha
user_login.voltar.clicked.connect(volta_func_user) # Botão para voltar a tela de login

# |=------------------------------------------------------------CD_FUNC--------------------------------------------------------------------------------------------------=| #

cd_func.inscrevase.clicked.connect(cadastro_func) # funçao cadastro cliente

cd_func.inscrevase.clicked.connect(chama_opçoes) # Botão de inscrever-se da tela de login

#cd_func.login.clicked.connect(volta_func_user) # Botão para chamar a tela de login

cd_func.voltar.clicked.connect(chama_opçoes)

cd_func.pesquisa.clicked.connect(alteracao_func)

# |=------------------------------------------------------------CD_USER--------------------------------------------------------------------------------------------------=| #

cd_user.inscrevase.clicked.connect(cadastro_cliente) # funçao cadastro cliente

cd_user.inscrevase.clicked.connect(chama_catalogo) # Botão de inscrever-se da tela de login

cd_user.login.clicked.connect(volta_func_user) # Botão para chamar a tela de login

# |=-------------------------------------------------------------CD_OPÇÔES-----------------------------------------------------------------------------------------------=| #

cd_opções.vendas.clicked.connect(chama_vendas) # Botão de 'cadastro de vendas' da tela de escolha para o cadastro de vendas

cd_opções.prod.clicked.connect(chama_produtos) # Botão de 'cadastro de produtos' da tela de escolha para o cadastro de produtos

cd_opções.voltar.clicked.connect(volta_login) # Botão 'voltar' da tela de escolha para a tela de login

#cd_opções.forne.clicked.connect(cd_fornecedor) # Botão 'cadastro de fornecedores'  na tela de escolha para a tela de fornecedores
 
cd_opções.func.clicked.connect(bt_pesquisar) # Botão de 'cadastro de cliente' na tela de escolha para a tela de cadastro de clientes

# |=----------------------------------------------------------------CD_PROD---------------------------------------------------------------------------------------------=| #

cd_prod.finalizar.clicked.connect(cadastro_prod) # Botão de 'voltar' da tela de cadastro de produtos para a tela de escolha

cd_prod.finalizar.clicked.connect(volta_op_prod) # Botão para chamar as opções apos cadastro de um produto

cd_prod.voltar.clicked.connect(volta_op_prod) # Botão de 'voltar' da tela de cadastro de vendas para a tela de escolha

# |=----------------------------------------------------------------CD_FORNECEDOR---------------------------------------------------------------------------------------=| #

cd_fornecedor.voltar.clicked.connect(volta_forn) # Botão de 'voltar' na tela de cadastro de fornecedores para a tela de cadastro de escolha

cd_fornecedor.finalizar.clicked.connect(cadastro_forn) # Botão para votar a tela de opçoes ao finalizar o cadastro de fornecedores


# |=------------------------------------------------------------------CATALOGO------------------------------------------------------------------------------------------=| #

catalogo.carrinho.clicked.connect(tela_pagamento) # Botão do carrinho para tela de pagamento

catalogo.user.clicked.connect(chama_user) #Botão para chamar tela do usuario

# |=------------------------------------------------------------------------TELA USUARIO--------------------------------------------------------------------------------=| #

tela_user.alt_dados.clicked.connect(alteracao) #Botão para chamar ediçao de dados

tela_user.catalogo.clicked.connect(chama_catalogo) #Botão para chamar catalogo

tela_user.sair.clicked.connect(sair) #Botão para sair

tela_user.del_dados.clicked.connect(delet) #Botão para chamar excluir dados

# |=------------------------------------------------------------------------ALT_DADOS-----------------------------------------------------------------------------------=| #

alt_dados.cancelar.clicked.connect(chama_user) #Botão para cancelar alteraçoes

# |=------------------------------------------------------------------------DELETAR_DADOS-------------------------------------------------------------------------------=| #

deletar.deletar.clicked.connect(confi_excluir) # Botão para deletar dados

deletar.cancelar.clicked.connect(volta_dados) # Botão para cancelar

# |=---------------------------------------------------------------------PAGAMENTOS-------------------------------------------------------------------------------------=| #

pagamentos.voltar.clicked.connect(voltar_catalogo) # Botão 'voltar' da tela de pagamento para o catalogo

# |=--------------------------------------------------------------------------------------------------------------------------------------------------------------------=| #


pre_login.show() # Tela inicial de login

app.exec() # Execução das janelas