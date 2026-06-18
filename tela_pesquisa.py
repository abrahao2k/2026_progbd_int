from PyQt5 import QtCore, QtGui, QtWidgets

import mariadb
conexao = mariadb.connect(host='localhost',user='root',
                          password='',database='copa2026')
cursor = conexao.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.pesquisar)
        
        self.verticalLayout.addWidget(self.pushButton)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pesquisa"))
        self.pushButton.setText(_translate("MainWindow", "PESQUISAR"))


    def pesquisar(self):
        info = self.lineEdit.text() # captura a digitação
        
        sql = f"""SELECT * FROM figurinhas
                  WHERE jogador LIKE '%{info}%'
                  OR pais LIKE '%{info}%'; """
        
        cursor.execute(sql)
        
        if cursor.rowcount == 0 :
            self.plainTextEdit.setPlainText(
                "Nenhum resultado.")
        else:
            dados = ""
            for linha in cursor:
                dados += "Código: " + str(linha[0]) + "\n"
                dados += "Jogador: " + linha[1] + "\n"
                dados += "País: " + linha[2] + "\n"
                dados += "-----------------------\n"
            
            dados += str(cursor.rowcount) + " resultados."
            
            self.plainTextEdit.setPlainText(dados)
            
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())