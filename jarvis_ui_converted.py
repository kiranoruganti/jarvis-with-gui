# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'futuristic_jarvis2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1439, 865)
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(1070, 30, 281, 61))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius :none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1441, 861))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/gifs/lib/bg gif.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_ = QtWidgets.QPushButton(Form)
        self.pushButton_.setGeometry(QtCore.QRect(1100, 720, 93, 31))
        self.pushButton_.setStyleSheet("background-color:rgb(255, 255, 0) ;\n"
"font: 75 16pt \"Nirmala UI\";\n"
"")
        self.pushButton_.setObjectName("pushButton_")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1190, 720, 93, 31))
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 0, 0);\n"
"font: 75 16pt \"Nirmala UI\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 90, 281, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/gifs/lib/neon_colour.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(1050, 70, 281, 101))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/gifs/lib/blue rotating bg.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(890, 200, 491, 491))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/gifs/lib/hologram.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(450, 350, 431, 261))
        self.label_6.setStyleSheet("background:transparent;\n"
"border-radius:none;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/gifs/lib/Jarvis_Gui (1).gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(70, 250, 321, 181))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/gifs/lib/Jarvis_Loading_Screen.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(80, 550, 301, 201))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/gifs/lib/Earth_Template.gif"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(1080, 90, 231, 61))
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(780, 70, 281, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/gifs/lib/blue rotating bg.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(810, 90, 221, 61))
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_.setText(_translate("Form", "Run"))
        self.pushButton_2.setText(_translate("Form", "Exit"))
        self.label_9.setText(_translate("Form", "TextLabel"))
        self.label_10.setText(_translate("Form", "TextLabel"))
import rec_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
