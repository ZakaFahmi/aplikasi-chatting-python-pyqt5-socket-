from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(324, 336)
        Form.setStyleSheet("background-color: rgb(255, 102, 0);\n"
"font: 57 8pt \"Poppins Medium\";\n"
"color: rgb(0, 0, 0)")
        self.hostTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.hostTextEdit.setGeometry(QtCore.QRect(123, 40, 130, 30))
        self.hostTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.hostTextEdit.setObjectName("hostTextEdit")
        self.portTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.portTextEdit.setGeometry(QtCore.QRect(123, 80, 131, 31))
        self.portTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.portTextEdit.setObjectName("portTextEdit")
        self.nameTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.nameTextEdit.setGeometry(QtCore.QRect(123, 120, 131, 31))
        self.nameTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.nameTextEdit.setObjectName("nameTextEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(125, 170, 90, 30))
        self.pushButton.setStyleSheet("background-color:rgb(51, 204, 255);\n"
"color:white;\n"
"border-radius:7px;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Hostname"))
        self.label_2.setText(_translate("Form", "Port"))
        self.label_3.setText(_translate("Form", "Name"))
        self.pushButton.setText(_translate("Form", "Connect"))


