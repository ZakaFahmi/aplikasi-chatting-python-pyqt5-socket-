from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(316, 504)
        Form.setStyleSheet("background-color: rgb(255, 102, 0);\n"
"font: 57 8pt \"Poppins Medium\";\n"
"color: rgb(0, 0, 0)")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 470, 300, 28))
        self.pushButton.setStyleSheet("background-color:rgb(51, 204, 255);\n"
"color:white;\n"
"border-radius:7px;")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 370, 300, 87))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 300, 350))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Send"))


