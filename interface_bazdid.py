# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bazdid.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 696)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/QIcon/Backup/iconn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color: #5D5136;\n"
"}\n"
"QStatusBar{\n"
"background-color:#5D5136;\n"
"color: rgb(0, 255, 59);\n"
"border:1px solid rgbrgb(0, 148, 0);\n"
"border-radius:2px;\n"
"    font: 10pt \"A Arsoo\";\n"
"}\n"
"QToolTip {\n"
"background-color: #b8d5dd;\n"
"    border: 2px solid  #1bff00 ;\n"
"    border-radius: 5px;\n"
"    color:  #e300a5 ;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setStatusTip("")
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab1_inputData = QtWidgets.QWidget()
        self.tab1_inputData.setWhatsThis("")
        self.tab1_inputData.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tab1_inputData.setStyleSheet("QWidget{\n"
"background-color: #b8d5dd  ;\n"
"}\n"
"QGroupBox{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"B Nazanin\";\n"
"border-style: dashed;\n"
"font-weight: bold;\n"
"border-bottom-width: 2px;\n"
"}\n"
"QRadioButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"A Arghavan\";\n"
"}\n"
"QLabel{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 17pt \"A Arsoo\";\n"
"}\n"
"QComboBox{\n"
"background-color: #eee1c5   ;\n"
"font: 75 10pt \"A Arsoo\";\n"
"color:#0A1F85;\n"
"border: 1px solid #096578  ;\n"
"border-radius: 3px;\n"
"}\n"
"QTextEdit{\n"
"background-color: #f9eff3 ;\n"
"font: 75 9pt \"A Arsoo\";\n"
"border: 1px solid  #fc9f47    ;\n"
"border-radius: 10px;\n"
"}\n"
"QCheckBox{\n"
"font: 75 12pt \"A Arsoo\";\n"
"}\n"
"QStatusBar{\n"
"background-color:rgb(33, 33, 33);\n"
"color: rgb(0, 255, 59);\n"
"border:1px solid rgbrgb(0, 148, 0);\n"
"border-radius:2px;\n"
"    font: 8pt \"Dast Nevis\";\n"
"}\n"
"")
        self.tab1_inputData.setObjectName("tab1_inputData")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab1_inputData)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_inputData = QtWidgets.QGroupBox(self.tab1_inputData)
        self.groupBox_inputData.setObjectName("groupBox_inputData")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_inputData)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_Sang = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Sang.setObjectName("horizontalLayout_Sang")
        spacerItem = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Sang.addItem(spacerItem)
        self.lineEdit_sangFari = QtWidgets.QLineEdit(self.groupBox_inputData)
        self.lineEdit_sangFari.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_sangFari.setFont(font)
        self.lineEdit_sangFari.setStatusTip("")
        self.lineEdit_sangFari.setStyleSheet("")
        self.lineEdit_sangFari.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sangFari.setObjectName("lineEdit_sangFari")
        self.horizontalLayout_Sang.addWidget(self.lineEdit_sangFari)
        self.label = QtWidgets.QLabel(self.groupBox_inputData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_Sang.addWidget(self.label)
        self.lineEdit_sangAsli = QtWidgets.QLineEdit(self.groupBox_inputData)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_sangAsli.setFont(font)
        self.lineEdit_sangAsli.setStatusTip("")
        self.lineEdit_sangAsli.setStyleSheet("")
        self.lineEdit_sangAsli.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_sangAsli.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_sangAsli.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sangAsli.setObjectName("lineEdit_sangAsli")
        self.horizontalLayout_Sang.addWidget(self.lineEdit_sangAsli)
        spacerItem1 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Sang.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_Sang, 0, 0, 1, 1)
        self.horizontalLayout_QRadio = QtWidgets.QHBoxLayout()
        self.horizontalLayout_QRadio.setContentsMargins(10, 7, 10, 7)
        self.horizontalLayout_QRadio.setSpacing(30)
        self.horizontalLayout_QRadio.setObjectName("horizontalLayout_QRadio")
        spacerItem2 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_QRadio.addItem(spacerItem2)
        self.lineEdit_moteqazi = QtWidgets.QLineEdit(self.groupBox_inputData)
        self.lineEdit_moteqazi.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_moteqazi.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_moteqazi.setObjectName("lineEdit_moteqazi")
        self.horizontalLayout_QRadio.addWidget(self.lineEdit_moteqazi)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_QRadio.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_QRadio, 1, 0, 1, 1)
        self.horizontalLayout_DarkhastKonande_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_DarkhastKonande_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_DarkhastKonande_3.setSpacing(10)
        self.horizontalLayout_DarkhastKonande_3.setObjectName("horizontalLayout_DarkhastKonande_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_DarkhastKonande_3.addItem(spacerItem4)
        self.label_11 = QtWidgets.QLabel(self.groupBox_inputData)
        self.label_11.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_11.setStatusTip("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_DarkhastKonande_3.addWidget(self.label_11)
        self.comboBox_noeAnjamKar = QtWidgets.QComboBox(self.groupBox_inputData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_noeAnjamKar.sizePolicy().hasHeightForWidth())
        self.comboBox_noeAnjamKar.setSizePolicy(sizePolicy)
        self.comboBox_noeAnjamKar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_noeAnjamKar.setStatusTip("")
        self.comboBox_noeAnjamKar.setEditable(True)
        self.comboBox_noeAnjamKar.setObjectName("comboBox_noeAnjamKar")
        self.comboBox_noeAnjamKar.addItem("")
        self.comboBox_noeAnjamKar.addItem("")
        self.comboBox_noeAnjamKar.addItem("")
        self.comboBox_noeAnjamKar.addItem("")
        self.comboBox_noeAnjamKar.addItem("")
        self.comboBox_noeAnjamKar.addItem("")
        self.comboBox_noeAnjamKar.addItem("")
        self.comboBox_noeAnjamKar.addItem("")
        self.comboBox_noeAnjamKar.addItem("")
        self.comboBox_noeAnjamKar.addItem("")
        self.horizontalLayout_DarkhastKonande_3.addWidget(self.comboBox_noeAnjamKar)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_DarkhastKonande_3.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.horizontalLayout_DarkhastKonande_3, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_inputData)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_DarkhastKonande = QtWidgets.QHBoxLayout()
        self.horizontalLayout_DarkhastKonande.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_DarkhastKonande.setSpacing(10)
        self.horizontalLayout_DarkhastKonande.setObjectName("horizontalLayout_DarkhastKonande")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_DarkhastKonande.addItem(spacerItem6)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_3.setStatusTip("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_DarkhastKonande.addWidget(self.label_3)
        self.comboBox_naghshebardar = QtWidgets.QComboBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_naghshebardar.sizePolicy().hasHeightForWidth())
        self.comboBox_naghshebardar.setSizePolicy(sizePolicy)
        self.comboBox_naghshebardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_naghshebardar.setStatusTip("")
        self.comboBox_naghshebardar.setEditable(True)
        self.comboBox_naghshebardar.setObjectName("comboBox_naghshebardar")
        self.comboBox_naghshebardar.addItem("")
        self.comboBox_naghshebardar.addItem("")
        self.horizontalLayout_DarkhastKonande.addWidget(self.comboBox_naghshebardar)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_DarkhastKonande.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_DarkhastKonande)
        self.horizontalLayout_DarkhastKonande_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_DarkhastKonande_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_DarkhastKonande_2.setSpacing(10)
        self.horizontalLayout_DarkhastKonande_2.setObjectName("horizontalLayout_DarkhastKonande_2")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_DarkhastKonande_2.addItem(spacerItem8)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_4.setStatusTip("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_DarkhastKonande_2.addWidget(self.label_4)
        self.comboBox_namaiande = QtWidgets.QComboBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_namaiande.sizePolicy().hasHeightForWidth())
        self.comboBox_namaiande.setSizePolicy(sizePolicy)
        self.comboBox_namaiande.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_namaiande.setStatusTip("")
        self.comboBox_namaiande.setEditable(True)
        self.comboBox_namaiande.setObjectName("comboBox_namaiande")
        self.comboBox_namaiande.addItem("")
        self.comboBox_namaiande.addItem("")
        self.comboBox_namaiande.addItem("")
        self.horizontalLayout_DarkhastKonande_2.addWidget(self.comboBox_namaiande)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_DarkhastKonande_2.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_DarkhastKonande_2)
        self.gridLayout_2.addWidget(self.groupBox_4, 3, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_inputData)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_3.setStatusTip("")
        self.groupBox_3.setStyleSheet("QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 12pt \"A Arghavan\";\n"
"border-style: solid;\n"
"border-bottom-width: 2px;\n"
"}\n"
"QCheckBox{\n"
"font: 75 8pt \"A Arsoo\";\n"
"}\n"
"QComboBox{\n"
"background-color: #eee1c5   ;\n"
"font: 75 10pt \"A Arsoo\";\n"
"color:#0A1F85;\n"
"border: 1px solid #096578  ;\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 1, 6, 1, 1)
        self.lineEdit_hour = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_hour.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_hour.sizePolicy().hasHeightForWidth())
        self.lineEdit_hour.setSizePolicy(sizePolicy)
        self.lineEdit_hour.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_hour.setMaximumSize(QtCore.QSize(50, 20))
        self.lineEdit_hour.setSizeIncrement(QtCore.QSize(20, 20))
        self.lineEdit_hour.setBaseSize(QtCore.QSize(20, 20))
        self.lineEdit_hour.setStatusTip("")
        self.lineEdit_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_hour.setObjectName("lineEdit_hour")
        self.gridLayout_8.addWidget(self.lineEdit_hour, 1, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 1, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_dateDay_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_dateDay_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_dateDay_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_dateDay_2.setSizePolicy(sizePolicy)
        self.lineEdit_dateDay_2.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateDay_2.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateDay_2.setSizeIncrement(QtCore.QSize(20, 20))
        self.lineEdit_dateDay_2.setBaseSize(QtCore.QSize(20, 20))
        self.lineEdit_dateDay_2.setStatusTip("")
        self.lineEdit_dateDay_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dateDay_2.setObjectName("lineEdit_dateDay_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_dateDay_2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(15, 46))
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdit_dateMonth_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_dateMonth_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_dateMonth_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_dateMonth_2.setSizePolicy(sizePolicy)
        self.lineEdit_dateMonth_2.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth_2.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth_2.setSizeIncrement(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth_2.setBaseSize(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth_2.setStatusTip("")
        self.lineEdit_dateMonth_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dateMonth_2.setObjectName("lineEdit_dateMonth_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_dateMonth_2)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(15, 46))
        self.label_10.setSizeIncrement(QtCore.QSize(15, 46))
        self.label_10.setBaseSize(QtCore.QSize(15, 46))
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.lineEdit_dateYear_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_dateYear_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_dateYear_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_dateYear_2.setSizePolicy(sizePolicy)
        self.lineEdit_dateYear_2.setMinimumSize(QtCore.QSize(35, 20))
        self.lineEdit_dateYear_2.setMaximumSize(QtCore.QSize(35, 20))
        self.lineEdit_dateYear_2.setSizeIncrement(QtCore.QSize(35, 20))
        self.lineEdit_dateYear_2.setBaseSize(QtCore.QSize(35, 20))
        self.lineEdit_dateYear_2.setStatusTip("")
        self.lineEdit_dateYear_2.setMaxLength(32765)
        self.lineEdit_dateYear_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dateYear_2.setObjectName("lineEdit_dateYear_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_dateYear_2)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 1, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem10, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem11, 1, 5, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem12, 1, 8, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.groupBox_Tozihat = QtWidgets.QGroupBox(self.groupBox_inputData)
        self.groupBox_Tozihat.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_Tozihat.setStatusTip("")
        self.groupBox_Tozihat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_Tozihat.setStyleSheet("QRadioButton{\n"
"font: 75 11pt \"A Arsoo\";\n"
"}")
        self.groupBox_Tozihat.setObjectName("groupBox_Tozihat")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_Tozihat)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textEdit_Tozihat = QtWidgets.QTextEdit(self.groupBox_Tozihat)
        self.textEdit_Tozihat.setEnabled(True)
        self.textEdit_Tozihat.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit_Tozihat.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_Tozihat.setStatusTip("")
        self.textEdit_Tozihat.setPlaceholderText("")
        self.textEdit_Tozihat.setObjectName("textEdit_Tozihat")
        self.gridLayout_6.addWidget(self.textEdit_Tozihat, 1, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_Tozihat, 5, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_sabtBtn = QtWidgets.QHBoxLayout()
        self.horizontalLayout_sabtBtn.setContentsMargins(20, 0, 20, 5)
        self.horizontalLayout_sabtBtn.setObjectName("horizontalLayout_sabtBtn")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_sabtBtn.addItem(spacerItem13)
        self.pushButton_sabt = QtWidgets.QPushButton(self.groupBox_inputData)
        self.pushButton_sabt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_sabt.setStatusTip("")
        self.pushButton_sabt.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed rgb(255, 85, 0);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: #FF0000;\n"
"}\n"
"QPushButton{\n"
"background-color: #24470d  ;\n"
"font: 14pt \"A Arsoo\";\n"
"color: rgb(255, 255, 127);\n"
"border: 1px solid   #b2ff00  ;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_sabt.setAutoDefault(False)
        self.pushButton_sabt.setDefault(False)
        self.pushButton_sabt.setObjectName("pushButton_sabt")
        self.horizontalLayout_sabtBtn.addWidget(self.pushButton_sabt)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_sabtBtn.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout_sabtBtn)
        self.horizontalLayout_btnNew = QtWidgets.QHBoxLayout()
        self.horizontalLayout_btnNew.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_btnNew.setObjectName("horizontalLayout_btnNew")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btnNew.addItem(spacerItem15)
        self.pushButton_new = QtWidgets.QPushButton(self.groupBox_inputData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_new.sizePolicy().hasHeightForWidth())
        self.pushButton_new.setSizePolicy(sizePolicy)
        self.pushButton_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_new.setStatusTip("")
        self.pushButton_new.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed   #039cff  ;\n"
"    background-color:  #cddbab  ;\n"
"    color:   #d101ff  ;\n"
"}\n"
"QPushButton{\n"
"background-color:   #0087f1    ;\n"
"font: 14pt \"A Arsoo\";\n"
"color: rgb(255, 255, 127);\n"
"border: 1px solid   #2bff01 ;;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_new.setObjectName("pushButton_new")
        self.horizontalLayout_btnNew.addWidget(self.pushButton_new)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btnNew.addItem(spacerItem16)
        self.verticalLayout.addLayout(self.horizontalLayout_btnNew)
        self.gridLayout_2.addLayout(self.verticalLayout, 6, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_inputData, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab1_inputData, "")
        self.tab2_SearchData = QtWidgets.QWidget()
        self.tab2_SearchData.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab2_SearchData.setStyleSheet("QWidget{\n"
"background-color: #ece6f9  ;\n"
"}\n"
"QGroupBox{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"B Nazanin\";\n"
"border-style: dashed;\n"
"font-weight: bold;\n"
"border-bottom-width: 2px;\n"
"}\n"
"QRadioButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"A Arghavan\";\n"
"}\n"
"QLabel{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 18pt \"A Arsoo\";\n"
"}\n"
"QComboBox{\n"
"background-color: #eee1c5   ;\n"
"}\n"
"QCheckBox{\n"
"font: 75 12pt \"A Arsoo\";\n"
"}\n"
"\n"
"QTableView {\n"
"padding: 4px;\n"
"border-style: none;\n"
"border-bottom: 1px solid #fffff8;\n"
"border-right: 1px solid #fffff8;\n"
"}\n"
"")
        self.tab2_SearchData.setObjectName("tab2_SearchData")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab2_SearchData)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab2_SearchData)
        self.groupBox.setEnabled(True)
        self.groupBox.setToolTip("")
        self.groupBox.setStatusTip("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_Sang_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Sang_2.setObjectName("horizontalLayout_Sang_2")
        spacerItem17 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Sang_2.addItem(spacerItem17)
        self.lineEdit_sangFari_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_sangFari_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_sangFari_2.setFont(font)
        self.lineEdit_sangFari_2.setStatusTip("")
        self.lineEdit_sangFari_2.setStyleSheet("")
        self.lineEdit_sangFari_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sangFari_2.setObjectName("lineEdit_sangFari_2")
        self.horizontalLayout_Sang_2.addWidget(self.lineEdit_sangFari_2)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_Sang_2.addWidget(self.label_6)
        self.lineEdit_sangAsli_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_sangAsli_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_sangAsli_2.setFont(font)
        self.lineEdit_sangAsli_2.setStatusTip("")
        self.lineEdit_sangAsli_2.setStyleSheet("")
        self.lineEdit_sangAsli_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_sangAsli_2.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_sangAsli_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sangAsli_2.setObjectName("lineEdit_sangAsli_2")
        self.horizontalLayout_Sang_2.addWidget(self.lineEdit_sangAsli_2)
        spacerItem18 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Sang_2.addItem(spacerItem18)
        self.gridLayout_7.addLayout(self.horizontalLayout_Sang_2, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_2.setStatusTip("")
        self.groupBox_2.setStyleSheet("QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 12pt \"A Arghavan\";\n"
"border-style: solid;\n"
"border-bottom-width: 2px;\n"
"}\n"
"QCheckBox{\n"
"font: 75 8pt \"A Arsoo\";\n"
"}\n"
"QComboBox{\n"
"background-color: #eee1c5   ;\n"
"font: 75 10pt \"A Arsoo\";\n"
"color:#0A1F85;\n"
"border: 1px solid #096578  ;\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_viaDate = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_viaDate.setStatusTip("")
        self.checkBox_viaDate.setObjectName("checkBox_viaDate")
        self.horizontalLayout_4.addWidget(self.checkBox_viaDate)
        spacerItem19 = QtWidgets.QSpacerItem(125, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem19)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_dateDay = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_dateDay.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_dateDay.sizePolicy().hasHeightForWidth())
        self.lineEdit_dateDay.setSizePolicy(sizePolicy)
        self.lineEdit_dateDay.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateDay.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateDay.setSizeIncrement(QtCore.QSize(20, 20))
        self.lineEdit_dateDay.setBaseSize(QtCore.QSize(20, 20))
        self.lineEdit_dateDay.setStatusTip("")
        self.lineEdit_dateDay.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dateDay.setObjectName("lineEdit_dateDay")
        self.horizontalLayout.addWidget(self.lineEdit_dateDay)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(15, 46))
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.lineEdit_dateMonth = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_dateMonth.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_dateMonth.sizePolicy().hasHeightForWidth())
        self.lineEdit_dateMonth.setSizePolicy(sizePolicy)
        self.lineEdit_dateMonth.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth.setSizeIncrement(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth.setBaseSize(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth.setStatusTip("")
        self.lineEdit_dateMonth.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dateMonth.setObjectName("lineEdit_dateMonth")
        self.horizontalLayout.addWidget(self.lineEdit_dateMonth)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(15, 46))
        self.label_8.setSizeIncrement(QtCore.QSize(15, 46))
        self.label_8.setBaseSize(QtCore.QSize(15, 46))
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEdit_dateYear = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_dateYear.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_dateYear.sizePolicy().hasHeightForWidth())
        self.lineEdit_dateYear.setSizePolicy(sizePolicy)
        self.lineEdit_dateYear.setMinimumSize(QtCore.QSize(35, 20))
        self.lineEdit_dateYear.setMaximumSize(QtCore.QSize(35, 20))
        self.lineEdit_dateYear.setSizeIncrement(QtCore.QSize(35, 20))
        self.lineEdit_dateYear.setBaseSize(QtCore.QSize(35, 20))
        self.lineEdit_dateYear.setStatusTip("")
        self.lineEdit_dateYear.setMaxLength(32765)
        self.lineEdit_dateYear.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dateYear.setObjectName("lineEdit_dateYear")
        self.horizontalLayout.addWidget(self.lineEdit_dateYear)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem20 = QtWidgets.QSpacerItem(164, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem20)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_viaName = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_viaName.setStatusTip("")
        self.checkBox_viaName.setObjectName("checkBox_viaName")
        self.horizontalLayout_5.addWidget(self.checkBox_viaName)
        spacerItem21 = QtWidgets.QSpacerItem(125, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem21)
        self.lineEdit_moteqazi_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_moteqazi_2.setEnabled(False)
        self.lineEdit_moteqazi_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_moteqazi_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"B Nazanin\";\n"
"border-style: dashed;\n"
"font-weight: bold;\n"
"border-bottom-width: 2px;")
        self.lineEdit_moteqazi_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_moteqazi_2.setObjectName("lineEdit_moteqazi_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_moteqazi_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem22 = QtWidgets.QSpacerItem(164, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem22)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, 1, 20, 1)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem23)
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_search.setEnabled(True)
        self.pushButton_search.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_search.setStatusTip("")
        self.pushButton_search.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed rgb(255, 85, 0);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton{\n"
"background-color: #d3f97a   ;\n"
"font: 14pt \"A Arsoo\";\n"
"color:    #056608   ;\n"
"border: 1px solid   #003efe   ;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_search.setAutoDefault(False)
        self.pushButton_search.setDefault(False)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_2.addWidget(self.pushButton_search)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem24)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.tableView_result = QtWidgets.QTableView(self.groupBox)
        self.tableView_result.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_result.sizePolicy().hasHeightForWidth())
        self.tableView_result.setSizePolicy(sizePolicy)
        self.tableView_result.setObjectName("tableView_result")
        self.gridLayout_7.addWidget(self.tableView_result, 3, 0, 1, 1)
        self.horizontalLayout_btnNew_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_btnNew_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_btnNew_2.setObjectName("horizontalLayout_btnNew_2")
        spacerItem25 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btnNew_2.addItem(spacerItem25)
        self.pushButton_print = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_print.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_print.sizePolicy().hasHeightForWidth())
        self.pushButton_print.setSizePolicy(sizePolicy)
        self.pushButton_print.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_print.setStatusTip("")
        self.pushButton_print.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed  #FF87A6  ;\n"
"    background-color:  #5F8375  ;\n"
"    color:  #E0F354  ;\n"
"}\n"
"QPushButton{\n"
"background-color:  #96B9B9    ;\n"
"font: 14pt \"A Arsoo\";\n"
"color: #533F11;\n"
"border: 1px solid   #FE760C ;;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_print.setObjectName("pushButton_print")
        self.horizontalLayout_btnNew_2.addWidget(self.pushButton_print)
        spacerItem26 = QtWidgets.QSpacerItem(100, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btnNew_2.addItem(spacerItem26)
        self.gridLayout_7.addLayout(self.horizontalLayout_btnNew_2, 4, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab2_SearchData, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_close = QtWidgets.QAction(MainWindow)
        self.action_close.setObjectName("action_close")
        self.action_ChangPassword = QtWidgets.QAction(MainWindow)
        self.action_ChangPassword.setObjectName("action_ChangPassword")
        self.action_backup = QtWidgets.QAction(MainWindow)
        self.action_backup.setObjectName("action_backup")
        self.menu.addAction(self.action_help)
        self.menu.addAction(self.action_ChangPassword)
        self.menu.addAction(self.action_backup)
        self.menu.addSeparator()
        self.menu.addAction(self.action_about)
        self.menu.addSeparator()
        self.menu.addAction(self.action_close)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.action_close.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.lineEdit_sangAsli)
        MainWindow.setTabOrder(self.lineEdit_sangAsli, self.lineEdit_sangFari)
        MainWindow.setTabOrder(self.lineEdit_sangFari, self.lineEdit_moteqazi)
        MainWindow.setTabOrder(self.lineEdit_moteqazi, self.comboBox_naghshebardar)
        MainWindow.setTabOrder(self.comboBox_naghshebardar, self.comboBox_namaiande)
        MainWindow.setTabOrder(self.comboBox_namaiande, self.lineEdit_dateDay_2)
        MainWindow.setTabOrder(self.lineEdit_dateDay_2, self.lineEdit_dateMonth_2)
        MainWindow.setTabOrder(self.lineEdit_dateMonth_2, self.lineEdit_dateYear_2)
        MainWindow.setTabOrder(self.lineEdit_dateYear_2, self.lineEdit_hour)
        MainWindow.setTabOrder(self.lineEdit_hour, self.textEdit_Tozihat)
        MainWindow.setTabOrder(self.textEdit_Tozihat, self.pushButton_sabt)
        MainWindow.setTabOrder(self.pushButton_sabt, self.pushButton_new)
        MainWindow.setTabOrder(self.pushButton_new, self.lineEdit_sangAsli_2)
        MainWindow.setTabOrder(self.lineEdit_sangAsli_2, self.lineEdit_sangFari_2)
        MainWindow.setTabOrder(self.lineEdit_sangFari_2, self.checkBox_viaDate)
        MainWindow.setTabOrder(self.checkBox_viaDate, self.lineEdit_dateDay)
        MainWindow.setTabOrder(self.lineEdit_dateDay, self.lineEdit_dateMonth)
        MainWindow.setTabOrder(self.lineEdit_dateMonth, self.lineEdit_dateYear)
        MainWindow.setTabOrder(self.lineEdit_dateYear, self.checkBox_viaName)
        MainWindow.setTabOrder(self.checkBox_viaName, self.lineEdit_moteqazi_2)
        MainWindow.setTabOrder(self.lineEdit_moteqazi_2, self.pushButton_search)
        MainWindow.setTabOrder(self.pushButton_search, self.pushButton_print)
        MainWindow.setTabOrder(self.pushButton_print, self.tableView_result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "تعیین وقت بازدید ثبت ماسال"))
        self.tab1_inputData.setStatusTip(_translate("MainWindow", "فرم ثبت تعیین وقت بازدید "))
        self.groupBox_inputData.setTitle(_translate("MainWindow", "فرم ثبت تعیین وقت بازدید"))
        self.lineEdit_sangFari.setToolTip(_translate("MainWindow", "<html><head/><body><p>سنگ <span style=\" font-weight:600; color:#724c00;\">فرعی</span> را وارد کنید</p></body></html>"))
        self.lineEdit_sangFari.setPlaceholderText(_translate("MainWindow", "سنگ فرعی"))
        self.label.setText(_translate("MainWindow", "/"))
        self.lineEdit_sangAsli.setToolTip(_translate("MainWindow", "<html><head/><body><p>سنگ <span style=\" font-weight:600; color:#875a00;\">اصلی</span> را وارد کنید</p></body></html>"))
        self.lineEdit_sangAsli.setPlaceholderText(_translate("MainWindow", "سنگ اصلی"))
        self.lineEdit_moteqazi.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">نام </span><span style=\" font-weight:600; color:#0000ff;\">متقاضی</span><span style=\" font-weight:600;\"> این پلاک را وارد کنید</span></p></body></html>"))
        self.lineEdit_moteqazi.setPlaceholderText(_translate("MainWindow", "نام متقاضی"))
        self.label_11.setToolTip(_translate("MainWindow", "نوع انجام کار روا مشخص کنید"))
        self.label_11.setText(_translate("MainWindow", "نوع انجام کار:"))
        self.comboBox_noeAnjamKar.setToolTip(_translate("MainWindow", "نوع انجام کار روا مشخص کنید"))
        self.comboBox_noeAnjamKar.setCurrentText(_translate("MainWindow", "تعویض سند"))
        self.comboBox_noeAnjamKar.setItemText(0, _translate("MainWindow", "تعویض سند"))
        self.comboBox_noeAnjamKar.setItemText(1, _translate("MainWindow", "المثنی"))
        self.comboBox_noeAnjamKar.setItemText(2, _translate("MainWindow", "اصلاح"))
        self.comboBox_noeAnjamKar.setItemText(3, _translate("MainWindow", "آپارتمان"))
        self.comboBox_noeAnjamKar.setItemText(4, _translate("MainWindow", "تفکیک"))
        self.comboBox_noeAnjamKar.setItemText(5, _translate("MainWindow", "تجمیع"))
        self.comboBox_noeAnjamKar.setItemText(6, _translate("MainWindow", "قانون تعیین تکلیف"))
        self.comboBox_noeAnjamKar.setItemText(7, _translate("MainWindow", "تحدید حدود اختصاصی"))
        self.comboBox_noeAnjamKar.setItemText(8, _translate("MainWindow", "بازدید"))
        self.comboBox_noeAnjamKar.setItemText(9, _translate("MainWindow", "سایر"))
        self.groupBox_4.setToolTip(_translate("MainWindow", "تعیین کردن نقشه بردار و نماینده اداره ثبت برای بازدید"))
        self.groupBox_4.setTitle(_translate("MainWindow", "تعیین نقشه بردار و نماینده"))
        self.label_3.setToolTip(_translate("MainWindow", "نقشه بردار را مشخص کنید"))
        self.label_3.setText(_translate("MainWindow", "نقشه بردار:"))
        self.comboBox_naghshebardar.setToolTip(_translate("MainWindow", "نقشه بردار را مشخص کنید"))
        self.comboBox_naghshebardar.setCurrentText(_translate("MainWindow", "کیوان حسنجانی"))
        self.comboBox_naghshebardar.setItemText(0, _translate("MainWindow", "کیوان حسنجانی"))
        self.comboBox_naghshebardar.setItemText(1, _translate("MainWindow", "سایر"))
        self.label_4.setToolTip(_translate("MainWindow", "نماینده را مشخص کنید"))
        self.label_4.setText(_translate("MainWindow", "نماینده:"))
        self.comboBox_namaiande.setToolTip(_translate("MainWindow", "نماینده را مشخص کنید"))
        self.comboBox_namaiande.setCurrentText(_translate("MainWindow", "سیدمحمد آتشی"))
        self.comboBox_namaiande.setItemText(0, _translate("MainWindow", "سیدمحمد آتشی"))
        self.comboBox_namaiande.setItemText(1, _translate("MainWindow", "علی رحمانی"))
        self.comboBox_namaiande.setItemText(2, _translate("MainWindow", "سایر"))
        self.groupBox_3.setToolTip(_translate("MainWindow", "تاریخ و ساعت بازدید"))
        self.groupBox_3.setTitle(_translate("MainWindow", "ثبت تاریخ و ساعت بازدید"))
        self.label_5.setText(_translate("MainWindow", "ساعت بازدید:"))
        self.lineEdit_hour.setToolTip(_translate("MainWindow", "ساعت"))
        self.lineEdit_hour.setPlaceholderText(_translate("MainWindow", "ساعت"))
        self.label_2.setText(_translate("MainWindow", "تاریخ بازدید:"))
        self.lineEdit_dateDay_2.setToolTip(_translate("MainWindow", "روز"))
        self.lineEdit_dateDay_2.setPlaceholderText(_translate("MainWindow", "روز"))
        self.label_9.setText(_translate("MainWindow", "/"))
        self.lineEdit_dateMonth_2.setToolTip(_translate("MainWindow", "ماه"))
        self.lineEdit_dateMonth_2.setPlaceholderText(_translate("MainWindow", "ماه"))
        self.label_10.setText(_translate("MainWindow", "/"))
        self.lineEdit_dateYear_2.setToolTip(_translate("MainWindow", "سال"))
        self.lineEdit_dateYear_2.setPlaceholderText(_translate("MainWindow", "سال"))
        self.groupBox_Tozihat.setToolTip(_translate("MainWindow", "  علت درخواست"))
        self.groupBox_Tozihat.setTitle(_translate("MainWindow", "توضیحات"))
        self.textEdit_Tozihat.setToolTip(_translate("MainWindow", "توضیحات خود را در این بخش بنویسید"))
        self.pushButton_sabt.setToolTip(_translate("MainWindow", "<html><head/><body><p dir=\"rtl\">برای ثبت کلیک کنید</p><p dir=\"rtl\">یا دکمه Enter را از کیبورد انتخاب کنید</p></body></html>"))
        self.pushButton_sabt.setText(_translate("MainWindow", "ثبت"))
        self.pushButton_new.setToolTip(_translate("MainWindow", "<html><head/><body><p dir=\"rtl\">پاکسازی فرم برای ثبت اطلاعات جدید</p><p dir=\"rtl\">کلید میانبر CTRL+N</p></body></html>"))
        self.pushButton_new.setText(_translate("MainWindow", "   جدید   "))
        self.pushButton_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1_inputData), _translate("MainWindow", "ورود اطلاعات"))
        self.tab2_SearchData.setStatusTip(_translate("MainWindow", " بازیابی پرونده های زمانبندی بازدید شده"))
        self.groupBox.setTitle(_translate("MainWindow", "فرم بازیابی اطلاعات ثبت شده"))
        self.lineEdit_sangFari_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>سنگ <span style=\" font-weight:600; color:#724c00;\">فرعی</span> را وارد کنید</p></body></html>"))
        self.lineEdit_sangFari_2.setPlaceholderText(_translate("MainWindow", "سنگ فرعی"))
        self.label_6.setText(_translate("MainWindow", "/"))
        self.lineEdit_sangAsli_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>سنگ <span style=\" font-weight:600; color:#875a00;\">اصلی</span> را وارد کنید</p></body></html>"))
        self.lineEdit_sangAsli_2.setPlaceholderText(_translate("MainWindow", "سنگ اصلی"))
        self.groupBox_2.setToolTip(_translate("MainWindow", "بازیابی پرونده های تعیین وقت شده به تاریخ"))
        self.groupBox_2.setTitle(_translate("MainWindow", "بازیابی پیشرفته"))
        self.checkBox_viaDate.setToolTip(_translate("MainWindow", "بازیابی سوابق ثبت شده به تاریخ"))
        self.checkBox_viaDate.setText(_translate("MainWindow", "بازیابی به تاریخ"))
        self.lineEdit_dateDay.setToolTip(_translate("MainWindow", "روز"))
        self.lineEdit_dateDay.setPlaceholderText(_translate("MainWindow", "روز"))
        self.label_7.setText(_translate("MainWindow", "/"))
        self.lineEdit_dateMonth.setToolTip(_translate("MainWindow", "ماه"))
        self.lineEdit_dateMonth.setPlaceholderText(_translate("MainWindow", "ماه"))
        self.label_8.setText(_translate("MainWindow", "/"))
        self.lineEdit_dateYear.setToolTip(_translate("MainWindow", "سال"))
        self.lineEdit_dateYear.setPlaceholderText(_translate("MainWindow", "سال"))
        self.checkBox_viaName.setToolTip(_translate("MainWindow", "بازیابی سوابق ثبت شده به نام متقاضی"))
        self.checkBox_viaName.setText(_translate("MainWindow", "بازیابی نام متقاضی"))
        self.lineEdit_moteqazi_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">نام </span><span style=\" font-weight:600; color:#0000ff;\">متقاضی</span><span style=\" font-weight:600;\"> این پلاک را وارد کنید</span></p></body></html>"))
        self.lineEdit_moteqazi_2.setPlaceholderText(_translate("MainWindow", "نام متقاضی"))
        self.pushButton_search.setToolTip(_translate("MainWindow", "برای بازیابی اطلاعات ذخیره شده کلیک کنید"))
        self.pushButton_search.setText(_translate("MainWindow", "جستجو"))
        self.pushButton_search.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.tableView_result.setToolTip(_translate("MainWindow", "نمایش نتیجه جستجو"))
        self.pushButton_print.setToolTip(_translate("MainWindow", "پرینت اطلاعات بازیابی شده"))
        self.pushButton_print.setText(_translate("MainWindow", "     پرینت     "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2_SearchData), _translate("MainWindow", "بازیابی اطلاعات"))
        self.menu.setTitle(_translate("MainWindow", "فایل"))
        self.action_help.setText(_translate("MainWindow", "راهنما"))
        self.action_about.setText(_translate("MainWindow", "درباره"))
        self.action_close.setText(_translate("MainWindow", "بستن"))
        self.action_ChangPassword.setText(_translate("MainWindow", "تغییر رمز ورود"))
        self.action_backup.setText(_translate("MainWindow", "پشتیبان گیری "))
        self.action_backup.setToolTip(_translate("MainWindow", "پشتیبان گیری از دیتابیس"))


import icon_rc
