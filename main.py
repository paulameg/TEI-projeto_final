from PyQt5 import  uic,QtWidgets
import sqlite3
import os.path

def chama_segunda_tela():
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE login ='{}'".format(nome_usuario))
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
        banco.close()
    except:
        print("Erro ao validar o login")

    try:
        if senha == senha_bd[0][0]:
            primeira_tela.close()
            segunda_tela.show()
        else :
            primeira_tela.label_4.setText("Dados de login incorretos!")
    except:
        primeira_tela.label_4.setText("Dados de login incorretos!")
    

def logout():
    segunda_tela.close()
    primeira_tela.show()

def abre_tela_cadastro():
    segunda_tela.close()
    tela_cadastro.show()

def abre_sobre():
    segunda_tela.close()
    tela_sobre.show()

def fecha_sobre():
    tela_sobre.close()
    segunda_tela.show()


def cadastrar():
    id = tela_cadastro.lineEdit_5.text()
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (id integer PRIMARY KEY, nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+id+"','"+nome+"','"+login+"','"+senha+"')")

            banco.commit() 
            banco.close()
            tela_cadastro.label_6.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cadastro.label_6.setText("As senhas digitadas estão diferentes")
    

def cadastrar_cifra():
    codigo = tela_cadastro_cifra.lineEdit.text()
    titulo = tela_cadastro_cifra.lineEdit_2.text()
    titulo_alt = tela_cadastro_cifra.lineEdit_3.text()
    artista = tela_cadastro_cifra.lineEdit_5.text()
    primeira_linha = tela_cadastro_cifra.lineEdit_6.text()
    primeira_linha_ref = tela_cadastro_cifra.lineEdit_4.text()
    tom = tela_cadastro_cifra.lineEdit_7.text()
    pagina = tela_cadastro_cifra.lineEdit_8.text()

    try:
        banco1 = sqlite3.connect('cadastro_cifras.db')
        cursor1 = banco1.cursor()
        cursor1.execute("""CREATE TABLE IF NOT EXISTS cadastro_cifras(
                            codigo integer PRIMARY KEY,
                            titulo text,
                            titulo_alt text,
                            artista text,
                            primeira_linha text,
                            primeira_linha_ref text,
                            tom text,
                            pagina integer
                            );""")
                            
        cursor1.execute("INSERT INTO cadastro_cifras VALUES ('"+codigo+"','"+titulo+"','"+titulo_alt+"','"+artista+"','"+primeira_linha+"','"+primeira_linha_ref+"','"+tom+"','"+pagina+"');")
        banco1.commit() 
        banco1.close()
        tela_cadastro_cifra.label_10.setText("Cifra cadastrada com sucesso!")
    
    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ",erro)
        tela_cadastro_cifra.label_10.setText("Erro ao cadastrar a cifra!")

def tela_cadastrar_cifra():
    segunda_tela.close()
    tela_cadastro_cifra.show()


def fechar_cadastrar_cifra():    
    tela_cadastro_cifra.close()
    segunda_tela.show()

def consultar_cifra():
    segunda_tela.close()
    tela_consultar_cifra.show()
    banco2 = sqlite3.connect('cadastro_cifras.db')
    cursor = banco2.cursor()
    cursor.execute("SELECT * FROM cadastro_cifras")
    dados_lidos = cursor.fetchall()
    tela_consultar_cifra.tableWidget.setRowCount(len(dados_lidos))
    tela_consultar_cifra.tableWidget.setColumnCount(8)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 8):
            tela_consultar_cifra.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
            #print(str(dados_lidos[i][j]))
    
    banco2.close()

def fechar_consulta_cifra():
    tela_consultar_cifra.close()
    segunda_tela.show()

def excluir_cifra():
    
    linha = tela_consultar_cifra.tableWidget.currentRow()
    tela_consultar_cifra.tableWidget.removeRow(linha)

    banco3 = sqlite3.connect('cadastro_cifras.db')
    cursor3 = banco3.cursor()
    cursor3.execute("SELECT codigo FROM cadastro_cifras")
    dados_lidos = cursor3.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor3.execute("DELETE FROM cadastro_cifras WHERE codigo="+ str(valor_id))
    banco3.commit()
    banco3.close()

    #print(valor_id)

def fechar_cadastrar():
    tela_cadastro.close()
    primeira_tela.show()

def tela_cadastrar_artista():
    segunda_tela.close()
    tela_cadastro_artista.show()

def cadastrar_artista():
    codigo1 = tela_cadastro_artista.lineEdit.text()
    nome1 = tela_cadastro_artista.lineEdit_2.text()
    idade1 = tela_cadastro_artista.lineEdit_3.text()
    local_nasc1 = tela_cadastro_artista.lineEdit_4.text()
    msc_famosa1 = tela_cadastro_artista.lineEdit_5.text()
    estilo1 = tela_cadastro_artista.lineEdit_6.text()

    try:
        banco4 = sqlite3.connect('cadastro_artistas.db')
        cursor4 = banco4.cursor()
        cursor4.execute("""CREATE TABLE IF NOT EXISTS cadastro_artistas(
                           codigo integer PRIMARY KEY,
                           nome text,
                           idade integer,
                           local_nasc text,
                           msc_famosa text,
                           estilo text);""")
    
        cursor4.execute("INSERT INTO cadastro_artistas VALUES ('"+codigo1+"','"+nome1+"','"+idade1+"','"+local_nasc1+"','"+msc_famosa1+"','"+estilo1+"')")

        banco4.commit()
        banco4.close()
        tela_cadastro_artista.label_8.setText("Artista cadastrado com sucesso!")
    
    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ", erro)
        tela_cadastro_artista.label_8.setText("Erro ao cadastrar artista!")

def consultar_artista():
    segunda_tela.close()
    tela_consultar_artista.show()
    banco = sqlite3.connect('cadastro_artistas.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastro_artistas")
    dados_lidos = cursor.fetchall()
    tela_consultar_artista.tableWidget.setRowCount(len(dados_lidos))
    tela_consultar_artista.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            tela_consultar_artista.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    banco.close()


def excluir_artista():
    linha = tela_consultar_artista.tableWidget.currentRow()
    tela_consultar_artista.tableWidget.removeRow(linha)

    banco = sqlite3.connect('cadastro_artistas.db')
    cursor = banco.cursor()
    cursor.execute("SELECT codigo FROM cadastro_artistas")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM cadastro_artistas WHERE codigo="+ str(valor_id))
    banco.commit()
    banco.close()

def fechar_cadastrar_artista():
    tela_cadastro_artista.close()
    segunda_tela.show()

def fechar_consultar_artista():
    tela_consultar_artista.close()
    segunda_tela.show()

def consultar_usuarios():
    segunda_tela.close()
    tela_listar_usuarios.show()
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastro")
    dados_lidos = cursor.fetchall()
    tela_listar_usuarios.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_usuarios.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            tela_listar_usuarios.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
            print(str(dados_lidos[i][j]))
    banco.close()

def fechar_listar_usuarios():
    tela_listar_usuarios.close()
    segunda_tela.show()

def excluir_usuario():
    linha = tela_listar_usuarios.tableWidget.currentRow()
    tela_listar_usuarios.tableWidget.removeRow(linha)

    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM cadastro WHERE id="+ str(valor_id))
    banco.commit()
    banco.close()

def abrir_mais_sobre():
    tela_sobre.close()
    tela_mais.show()

def fechar_mais_sobre():
    tela_mais.close()
    tela_sobre.show()

app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
tela_sobre = uic.loadUi("Sobre.ui")
tela_cadastro_cifra = uic.loadUi("cadastro_cifra.ui")
tela_consultar_cifra = uic.loadUi("listar_cifras.ui")
tela_cadastro_artista = uic.loadUi("cadastro_artista.ui")
tela_consultar_artista = uic.loadUi("listar_artistas.ui")
tela_listar_usuarios = uic.loadUi("listar_usuarios.ui")
tela_mais = uic.loadUi("mais_sobre.ui")

primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(logout)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar) 
segunda_tela.pushButton_2.clicked.connect(abre_sobre)
tela_sobre.pushButton.clicked.connect(fecha_sobre)
segunda_tela.pushButton_3.clicked.connect(tela_cadastrar_cifra)
tela_cadastro_cifra.pushButton.clicked.connect(fechar_cadastrar_cifra)
tela_cadastro_cifra.pushButton_2.clicked.connect(cadastrar_cifra)
segunda_tela.pushButton_4.clicked.connect(consultar_cifra)
tela_consultar_cifra.pushButton_2.clicked.connect(fechar_consulta_cifra)
tela_consultar_cifra.pushButton_3.clicked.connect(excluir_cifra)
tela_cadastro.pushButton_3.clicked.connect(fechar_cadastrar)
segunda_tela.pushButton_5.clicked.connect(tela_cadastrar_artista)
tela_cadastro_artista.pushButton_2.clicked.connect(cadastrar_artista)
segunda_tela.pushButton_6.clicked.connect(consultar_artista)
tela_consultar_artista.pushButton_3.clicked.connect(excluir_artista)
tela_cadastro_artista.pushButton.clicked.connect(fechar_cadastrar_artista)
tela_consultar_artista.pushButton_2.clicked.connect(fechar_consultar_artista)
segunda_tela.pushButton_7.clicked.connect(consultar_usuarios)
tela_listar_usuarios.pushButton_2.clicked.connect(fechar_listar_usuarios)
tela_listar_usuarios.pushButton_3.clicked.connect(excluir_usuario)
tela_sobre.pushButton_2.clicked.connect(abrir_mais_sobre)
tela_mais.pushButton.clicked.connect(fechar_mais_sobre)

primeira_tela.show()
app.exec()