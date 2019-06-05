# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(288, 144)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setStyleSheet("QWidget{\n"
"background-color:#396BFE;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_creator = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_creator.setFont(font)
        self.label_creator.setStyleSheet("color: #FC9D00;")
        self.label_creator.setAlignment(QtCore.Qt.AlignCenter)
        self.label_creator.setObjectName("label_creator")
        self.horizontalLayout.addWidget(self.label_creator)
        self.label_sarbaz = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("A Chamran")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_sarbaz.setFont(font)
        self.label_sarbaz.setStyleSheet("color:  #23FF00;")
        self.label_sarbaz.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sarbaz.setObjectName("label_sarbaz")
        self.horizontalLayout.addWidget(self.label_sarbaz)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label_email = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_email.setFont(font)
        self.label_email.setStyleSheet("color:#E6F014 ;")
        self.label_email.setAlignment(QtCore.Qt.AlignCenter)
        self.label_email.setObjectName("label_email")
        self.gridLayout.addWidget(self.label_email, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "درباره "))
        Form.setToolTip(_translate("Form", "<html><head/><body><p dir=\'rtl\'>برای بستن این پنجره بر روی کیبورد کلید Enter را بفشارید.</p></body></html>"))
        self.label_creator.setText(_translate("Form", "توسعه داده شده توسط : "))
        self.label_sarbaz.setText(_translate("Form", "سرباز"))
        self.label_email.setToolTip(_translate("Form", "<html><head/><body><p dir=\'rtl\'><span style=\" color:#55007f;\">برای ارتباط با سازنده کلیک کنید.</span></p></body></html>"))
        self.label_email.setText(_translate("Form", "<html><head/><body><p><a href=\"mailto:s.a.e.i.d@live.com?subject=ارتباط%20با%20سازنده%20سامانه%20بایگانی%20ثبت%20ماسال\"><span style=\"text-decoration: none; color:#00ffff;\">© 1398 | sjavadip@gmail.com</span></a></p></body></html>"))


