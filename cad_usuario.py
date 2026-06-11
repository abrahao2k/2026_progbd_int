from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox    # para criar janela diálogo

### CONEXÃO B.D. ##################
import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="sistematop")
cursor = conexao.cursor()
###################################

class Ui_CadastroUsuario(object):
    def setupUi(self, CadastroUsuario):
        CadastroUsuario.setObjectName("CadastroUsuario")
        CadastroUsuario.resize(290, 120)
        self.centralwidget = QtWidgets.QWidget(CadastroUsuario)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_usuario = QtWidgets.QLabel(self.centralwidget)
        self.label_usuario.setObjectName("label_usuario")
        self.gridLayout.addWidget(self.label_usuario, 0, 0, 1, 1)
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.gridLayout.addWidget(self.lineEdit_usuario, 0, 1, 1, 1)
        self.label_senha = QtWidgets.QLabel(self.centralwidget)
        self.label_senha.setObjectName("label_senha")
        self.gridLayout.addWidget(self.label_senha, 1, 0, 1, 1)
        self.lineEdit_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.gridLayout.addWidget(self.lineEdit_senha, 1, 1, 1, 1)
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        
        ### liga o botão com a função ####################################
        self.pushButton_salvar.clicked.connect(self.cadastrar)
        
        self.gridLayout.addWidget(self.pushButton_salvar, 2, 1, 1, 1)
        CadastroUsuario.setCentralWidget(self.centralwidget)

        self.retranslateUi(CadastroUsuario)
        QtCore.QMetaObject.connectSlotsByName(CadastroUsuario)

    def retranslateUi(self, CadastroUsuario):
        _translate = QtCore.QCoreApplication.translate
        CadastroUsuario.setWindowTitle(_translate("CadastroUsuario", "Cadastro de Usuário"))
        self.label_usuario.setText(_translate("CadastroUsuario", "Usuário:"))
        self.label_senha.setText(_translate("CadastroUsuario", "Senha:"))
        self.pushButton_salvar.setText(_translate("CadastroUsuario", "SALVAR"))


    def cadastrar(self):
        usu = self.lineEdit_usuario.text()  # captura a digitação
        sen = self.lineEdit_senha.text()    # captura a digitação
        
        sql=f'''INSERT INTO usuarios VALUES
                (null, '{usu}', MD5('{sen}') ); '''
        
        cursor.execute(sql)
        conexao.commit()
        
        msg = QMessageBox()   # cria dialogo vazio
        msg.setText("Gravado com sucesso.") # define o texto
        msg.setWindowTitle("Aviso") # titulo da janela
        msg.setIcon(QMessageBox.Information)  # icone
                    # Question, Critical, Warning
        msg.exec_() # exibe
        
        self.lineEdit_usuario.setText("")  # limpar
        self.lineEdit_senha.setText("")
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CadastroUsuario = QtWidgets.QMainWindow()
    ui = Ui_CadastroUsuario()
    ui.setupUi(CadastroUsuario)
    CadastroUsuario.show()
    sys.exit(app.exec_())