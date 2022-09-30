def alteracao_tabela_cliente(): 
    
    alter_meiri.show()
    

    cursor = connect.cursor()
    sql = "Select * from cd_user"
    cursor.execute(sql)

    leitura_sql = cursor.fetchall()

    alter_meiri.tableWidget.setRowCount(len(leitura_sql)) #tabela de clientes
    alter_meiri.tableWidget.setColumnCount(9) # colunas preenchidas na lista de cliente

    for i in range(0, len(leitura_sql)):
        for j in range(0, 9):
            alter_meiri.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_sql[i][j]))) # preenchimento das linhas e colunas

def excluir_dados_tabela_cliente(): 

    linha =  alter_meiri.tableWidget.currentRow() # linha selecionada
    alter_meiri.tableWidget.removeRow(linha) # remoção da linha

    cursor = connect.cursor()
    cursor.execute('SELECT id FROM cd_user')
    execute_sql = cursor.fetchall()
    valor_id = execute_sql[linha][0]
    cursor.execute("DELETE FROM cd_user WHERE id = " + str(valor_id))

    connect.commit()

    cursor.close()

    alter_meiri.hide()
    alter_meiri.show()


def edicao_dados_tabela_cliente(): 

    cd_opções.hide()

    linha =  alter_meiri.tableWidget.currentRow()
    

    cursor = connect.cursor()
    cursor.execute('SELECT id FROM cd_user')
    execute_sql = cursor.fetchall()
    valor_id = execute_sql[linha][0]
    cursor.execute("SELECT * FROM cd_user WHERE id = " + str(valor_id))
    editar = cursor.fetchall()
    edit_meiri.show()

    

    edit_meiri.edit_cod.setText(str(editar[0][0]))
    edit_meiri.edit_nome.setText(str(editar[0][1]))
    edit_meiri.edit_email.setText(str(editar[0][2]))
    edit_meiri.edit_senha.setText(str(editar[0][3]))
    edit_meiri.edit_cep.setText(str(editar[0][4]))
    edit_meiri.edit_tel.setText(str(editar[0][5]))
    edit_meiri.edit_ende.setText(str(editar[0][6]))
    edit_meiri.edit_nasc.setText(str(editar[0][7]))
    edit_meiri.edit_cpf.setText(str(editar[0][8]))


def salvar_dados_editados_tabela_cliente():


    codl = edit_meiri.edit_cod.text()
    nomel = edit_meiri.edit_nome.text()
    emaill = edit_meiri.edit_email.text()
    senhal = edit_meiri.edit_senha.text()
    cepl = edit_meiri.edit_cep.text()
    telefonel = edit_meiri.edit_tel.text()
    enderecol = edit_meiri.edit_ende.text()
    nascl = edit_meiri.edit_nasc.text()
    cpfl = edit_meiri.edit_cpf.text()

    cursor = connect.cursor()
   
    atualizar ="UPDATE cd_user SET nome = '{}', email = '{}', senha = '{}', cep = '{}', telefone = '{}', endereco = '{}', nasc = '{}', cpf = '{}' where id = '{}' ".format (nomel,emaill,senhal,cepl, telefonel, enderecol, nascl, cpfl, codl)
    cursor.execute(atualizar)

    QtWidgets.QMessageBox.about(edit_meiri, 'Sucesso', 'Atualização feito com sucesso!')

    connect.commit()
    
    alter_meiri.close()
    edit_meiri.close()
    cd_opções.show()

===========================================================================================================================================================

alter_meiri=uic.loadUi('meiri-alter.ui') # Inicializador da tela de login
edit_meiri=uic.loadUi('editardados.ui')

===========================================================================================================================================================

cd_opções.exc_clientes.clicked.connect(alteracao_tabela_cliente)

alter_meiri.alter_excluir.clicked.connect(excluir_dados_tabela_cliente)

alter_meiri.alter_editar.clicked.connect(edicao_dados_tabela_cliente)

edit_meiri.edit_salvar.clicked.connect(salvar_dados_editados_tabela_cliente)