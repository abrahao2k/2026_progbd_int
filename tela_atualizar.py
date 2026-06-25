from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox

import mariadb
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="copa2026")
cursor = conexao.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 164)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_codigo = QtWidgets.QLabel(self.centralwidget)
        self.label_codigo.setObjectName("label_codigo")
        self.gridLayout.addWidget(self.label_codigo, 0, 0, 1, 1)
        self.lineEdit_codigo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_codigo.setObjectName("lineEdit_codigo")
        self.gridLayout.addWidget(self.lineEdit_codigo, 0, 1, 1, 1)
        
        self.pushButton_abrir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_abrir.setObjectName("pushButton_abrir")
        self.pushButton_abrir.clicked.connect(self.abrir)
        
        self.gridLayout.addWidget(self.pushButton_abrir, 0, 2, 1, 1)
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 1, 0, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 1, 1, 1, 1)
        self.label_pais = QtWidgets.QLabel(self.centralwidget)
        self.label_pais.setObjectName("label_pais")
        self.gridLayout.addWidget(self.label_pais, 2, 0, 1, 1)
        self.lineEdit_pais = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pais.setObjectName("lineEdit_pais")
        self.gridLayout.addWidget(self.lineEdit_pais, 2, 1, 1, 1)
        
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.pushButton_salvar.clicked.connect(self.salvar)
        
        self.gridLayout.addWidget(self.pushButton_salvar, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATUALIZAR"))
        self.label_codigo.setText(_translate("MainWindow", "Código:"))
        self.pushButton_abrir.setText(_translate("MainWindow", "ABRIR"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_pais.setText(_translate("MainWindow", "País:"))
        self.pushButton_salvar.setText(_translate("MainWindow", "SALVAR"))

    def abrir(self):
        cod = self.lineEdit_codigo.text()  # captura a digitação
        sql = "SELECT * FROM figurinhas WHERE codigo = " + cod
        cursor.execute(sql)
        
        if cursor.rowcount == 0:  # não achou
            QMessageBox.information(None,"Aviso","Código inválido")
            self.lineEdit_nome.clear() # limpa o campo
            self.lineEdit_pais.clear()
            
        else: # achou
            # (1, "Alisson", "Brasil")
            #  0      1         2
            
            dados = cursor.fetchone() # transfere 1 registro
            self.lineEdit_nome.setText(dados[1])
            self.lineEdit_pais.setText(dados[2])
            self.lineEdit_codigo.setReadOnly(True) # bloqueia o campo

    def salvar(self):
        cod  = self.lineEdit_codigo.text()
        nome = self.lineEdit_nome.text()
        pais = self.lineEdit_pais.text()
        
        sql = f'''UPDATE figurinhas SET
                  jogador = '{nome}',
                  pais = '{pais}'
                  WHERE codigo = {cod}; '''
        
        cursor.execute(sql)
        conexao.commit()
        QMessageBox.information(None,"Aviso","Atualizado com sucesso.")
        
        self.lineEdit_nome.clear()
        self.lineEdit_pais.clear()
        self.lineEdit_codigo.setReadOnly(False) #libera o campo



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())