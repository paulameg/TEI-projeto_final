from PyQt5 import  uic,QtWidgets
import sqlite3


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
    tela_cadastro.show()

def abre_sobre():
    segunda_tela.close()
    tela_sobre.show()

def fecha_sobre():
    tela_sobre.close()
    segunda_tela.show()


def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+login+"','"+senha+"')")

            banco.commit() 
            banco.close()
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")
    

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




app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
tela_sobre = uic.loadUi("Sobre.ui")
tela_cadastro_cifra = uic.loadUi("cadastro_cifra.ui")

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

primeira_tela.show()
app.exec()