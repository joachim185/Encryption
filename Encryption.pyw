from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtText = QtWidgets.QLineEdit(self.centralwidget)
        self.txtText.setGeometry(QtCore.QRect(270, 30, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtText.setFont(font)
        self.txtText.setText("")
        self.txtText.setObjectName("txtText")
        self.txtPasswd = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPasswd.setGeometry(QtCore.QRect(270, 90, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPasswd.setFont(font)
        self.txtPasswd.setObjectName("txtPasswd")
        self.lblText = QtWidgets.QLabel(self.centralwidget)
        self.lblText.setGeometry(QtCore.QRect(140, 30, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.lblText.setFont(font)
        self.lblText.setObjectName("lblText")
        self.lblPasswd = QtWidgets.QLabel(self.centralwidget)
        self.lblPasswd.setGeometry(QtCore.QRect(130, 90, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.lblPasswd.setFont(font)
        self.lblPasswd.setObjectName("lblPasswd")
        self.txtOut = QtWidgets.QTextEdit(self.centralwidget)
        self.txtOut.setGeometry(QtCore.QRect(10, 240, 781, 301))
        self.txtOut.setObjectName("txtOut")
        self.btbEnc = QtWidgets.QPushButton(self.centralwidget)
        self.btbEnc.setGeometry(QtCore.QRect(160, 170, 171, 51))
        self.btbEnc.setObjectName("btbEnc")
        self.btbDecry = QtWidgets.QPushButton(self.centralwidget)
        self.btbDecry.setGeometry(QtCore.QRect(440, 170, 171, 51))
        self.btbDecry.setObjectName("btbDecry")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblText.setText(_translate("MainWindow", "Text: "))
        self.lblPasswd.setText(_translate("MainWindow", "Password: "))
        self.txtOut.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btbEnc.setText(_translate("MainWindow", "Encrypt"))
        self.btbDecry.setText(_translate("MainWindow", "Decrypt"))
        self.btbEnc.clicked.connect(self.enc)
        self.btbDecry.clicked.connect(self.dec)

    def enc(self):
        pwd=self.txtPasswd.text()
        txt=self.txtText.text()
        abc="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZßöäüÖÄÜ,.-;:_<>|!§$%&/()=?1234567890+*~#"
        aus=""
        j=0
        for i in txt:
            try:
                y=abc.index(pwd[j])
            except :
                j=0

            x=abc.index(i)

            try:
                aus=aus+abc[x+y]
            except :
                aus=aus+abc[(x+y)-93]

            j=j+1

        j=0

        self.txtOut.setText(aus)

    def dec(self):
        pwd=self.txtPasswd.text()
        txt=self.txtText.text()
        abc="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZßöäüÖÄÜ,.-;:_<>|!§$%&/()=?1234567890+*~#"
        dec=""
        j=0

        for k in txt:
            try:
                y=abc.index(pwd[j])
            except :
                j=0

            try:
                x=abc.index(k)
                dec=dec+abc[x-y]
            except :
                dec=dec+abc[(x-y)]

            j=j+1


        self.txtOut.setText(dec)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
