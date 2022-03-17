# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 238)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(78, 78, 116);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 10, 65, 21))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.label_2.setTextFormat(Qt.AutoText)
        self.opcU1_LB = QLabel(Form)
        self.opcU1_LB.setObjectName(u"opcU1_LB")
        self.opcU1_LB.setGeometry(QRect(50, 40, 100, 90))
        self.opcU1_LB.setStyleSheet(u"QLabel{\n"
"	border: 2px outset white;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(81, 81, 61);\n"
"}")
        self.opcU1_LB.setFrameShape(QFrame.NoFrame)
        self.opcU1_LB.setScaledContents(True)
        self.opciones_CB = QComboBox(Form)
        self.opciones_CB.addItem("")
        self.opciones_CB.addItem("")
        self.opciones_CB.addItem("")
        self.opciones_CB.addItem("")
        self.opciones_CB.setObjectName(u"opciones_CB")
        self.opciones_CB.setEnabled(True)
        self.opciones_CB.setGeometry(QRect(130, 150, 124, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opciones_CB.sizePolicy().hasHeightForWidth())
        self.opciones_CB.setSizePolicy(sizePolicy)
        self.opciones_CB.setMinimumSize(QSize(82, 0))
        self.opciones_CB.setBaseSize(QSize(399, 240))
        palette = QPalette()
        brush = QBrush(QColor(58, 222, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(104, 104, 78, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(58, 222, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush3 = QBrush(QColor(81, 81, 61, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush4 = QBrush(QColor(58, 222, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush5 = QBrush(QColor(58, 222, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.opciones_CB.setPalette(palette)
        font1 = QFont()
        font1.setFamily(u"Verdana")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.opciones_CB.setFont(font1)
        self.opciones_CB.setCursor(QCursor(Qt.PointingHandCursor))
        self.opciones_CB.setLayoutDirection(Qt.LeftToRight)
        self.opciones_CB.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 1 px;\n"
"	font: 8pt \"Verdana\";\n"
"	color: rgb(58, 222, 255);\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgba(88, 66, 255, 160);\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background-color: rgb(104, 104, 78);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	 background-color: rgb(81, 81, 61);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 rgb(104, 104, 78), stop: 0.4 rgb(104, 104, 78),\n"
"                                stop: 0.5 rgb(120, 104, 78), stop: 1.0  rgb(104, 104, 78) );\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 40px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:pressed { /* shift the arrow when popup is open */\n"
" "
                        "   position: relative;\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.opciones_CB.setEditable(False)
        self.opciones_CB.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.opciones_CB.setIconSize(QSize(0, 0))
        self.opciones_CB.setFrame(True)
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 180, 30, 20))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(10)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 115, 0);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}\n"
"\n"
"/*rgb(255, 119, 0)*/")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.cantELoc_LB = QLabel(Form)
        self.cantELoc_LB.setObjectName(u"cantELoc_LB")
        self.cantELoc_LB.setGeometry(QRect(90, 200, 30, 20))
        self.cantELoc_LB.setFont(font2)
        self.cantELoc_LB.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}")
        self.cantELoc_LB.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(90, 180, 30, 20))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 255, 149);\n"
"	border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.cantPLoc_LB = QLabel(Form)
        self.cantPLoc_LB.setObjectName(u"cantPLoc_LB")
        self.cantPLoc_LB.setGeometry(QRect(60, 200, 30, 20))
        self.cantPLoc_LB.setFont(font2)
        self.cantPLoc_LB.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}")
        self.cantPLoc_LB.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 160, 91, 16))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setItalic(True)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"\n"
"}")
        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 180, 30, 20))
        self.label_17.setFont(font2)
        self.label_17.setLayoutDirection(Qt.LeftToRight)
        self.label_17.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 127);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.cantGLoc_LB = QLabel(Form)
        self.cantGLoc_LB.setObjectName(u"cantGLoc_LB")
        self.cantGLoc_LB.setGeometry(QRect(30, 200, 30, 20))
        self.cantGLoc_LB.setFont(font2)
        self.cantGLoc_LB.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}")
        self.cantGLoc_LB.setAlignment(Qt.AlignCenter)
        self.msjGame_LB = QLabel(Form)
        self.msjGame_LB.setObjectName(u"msjGame_LB")
        self.msjGame_LB.setGeometry(QRect(130, 190, 160, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        font4.setKerning(True)
        self.msjGame_LB.setFont(font4)
        self.msjGame_LB.setAutoFillBackground(False)
        self.msjGame_LB.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"	border: 1px solid white;\n"
"	border-radius: 100%;\n"
"	background-color: rgba(255, 255, 255, 250);\n"
"}")
        self.msjGame_LB.setFrameShape(QFrame.StyledPanel)
        self.msjGame_LB.setFrameShadow(QFrame.Plain)
        self.msjGame_LB.setLineWidth(1)
        self.msjGame_LB.setScaledContents(False)
        self.msjGame_LB.setAlignment(Qt.AlignCenter)
        self.msjGame_LB.setWordWrap(False)
        self.msjGame_LB.setIndent(-1)
        self.jugar_PB = QPushButton(Form)
        self.jugar_PB.setObjectName(u"jugar_PB")
        self.jugar_PB.setGeometry(QRect(280, 130, 70, 30))
        font5 = QFont()
        font5.setFamily(u"Verdana")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.jugar_PB.setFont(font5)
        self.jugar_PB.setCursor(QCursor(Qt.PointingHandCursor))
        self.jugar_PB.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(81, 81, 61);\n"
"	font: 10pt \"Verdana\";\n"
"	color: rgb(58, 222, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 rgb(104, 104, 78), stop: 1 rgb(104, 104, 78) );\n"
"}\n"
"\n"
"\n"
"")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 30, 30, 20))
        font6 = QFont()
        font6.setPointSize(11)
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 115, 0);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}\n"
"\n"
"/*rgb(255, 119, 0)*/")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.cantGS_LB = QLabel(Form)
        self.cantGS_LB.setObjectName(u"cantGS_LB")
        self.cantGS_LB.setGeometry(QRect(270, 50, 30, 20))
        self.cantGS_LB.setFont(font6)
        self.cantGS_LB.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}")
        self.cantGS_LB.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(330, 30, 30, 20))
        self.label_15.setFont(font6)
        self.label_15.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 255, 149);\n"
"	border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.cantPS_LB = QLabel(Form)
        self.cantPS_LB.setObjectName(u"cantPS_LB")
        self.cantPS_LB.setGeometry(QRect(300, 50, 30, 20))
        self.cantPS_LB.setFont(font6)
        self.cantPS_LB.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}")
        self.cantPS_LB.setAlignment(Qt.AlignCenter)
        self.cantES_LB = QLabel(Form)
        self.cantES_LB.setObjectName(u"cantES_LB")
        self.cantES_LB.setGeometry(QRect(330, 50, 30, 20))
        self.cantES_LB.setFont(font6)
        self.cantES_LB.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}")
        self.cantES_LB.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(270, 30, 30, 20))
        self.label_12.setFont(font6)
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 127);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"	border-radius: 100px;\n"
"}")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.msjSys_LB = QLabel(Form)
        self.msjSys_LB.setObjectName(u"msjSys_LB")
        self.msjSys_LB.setGeometry(QRect(340, 190, 160, 31))
        self.msjSys_LB.setFont(font4)
        self.msjSys_LB.setAutoFillBackground(False)
        self.msjSys_LB.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	border: 1px solid rgba(255, 255, 255, 50);\n"
"	border-radius: 100%;\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"}")
        self.msjSys_LB.setFrameShape(QFrame.StyledPanel)
        self.msjSys_LB.setFrameShadow(QFrame.Plain)
        self.msjSys_LB.setLineWidth(1)
        self.msjSys_LB.setTextFormat(Qt.MarkdownText)
        self.msjSys_LB.setScaledContents(False)
        self.msjSys_LB.setAlignment(Qt.AlignCenter)
        self.msjSys_LB.setWordWrap(True)
        self.msjSys_LB.setIndent(-1)
        self.opcU2_LB = QLabel(Form)
        self.opcU2_LB.setObjectName(u"opcU2_LB")
        self.opcU2_LB.setGeometry(QRect(490, 40, 100, 90))
        self.opcU2_LB.setStyleSheet(u"QLabel{\n"
"	border: 2px outset white;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(81, 81, 61);\n"
"}")
        self.opcU2_LB.setFrameShape(QFrame.NoFrame)
        self.opcU2_LB.setScaledContents(True)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(510, 10, 65, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"}")
        self.cerrar_PB = QPushButton(Form)
        self.cerrar_PB.setObjectName(u"cerrar_PB")
        self.cerrar_PB.setGeometry(QRect(520, 190, 75, 23))
        self.cerrar_PB.setCursor(QCursor(Qt.PointingHandCursor))
        self.cerrar_PB.setAutoFillBackground(False)
        self.cerrar_PB.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(170, 0, 0);\n"
"	font: 10pt \"Verdana\";\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 rgb(255, 85, 0), stop: 1 rgb(255, 85, 0) );\n"
"}")
        self.cerrar_PB.setAutoDefault(False)
        self.cerrar_PB.setFlat(False)

        self.retranslateUi(Form)

        self.cerrar_PB.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Piedra, papel, tijera :)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Jugador 1", None))
#if QT_CONFIG(whatsthis)
        self.opcU1_LB.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.opcU1_LB.setText("")
        self.opciones_CB.setItemText(0, QCoreApplication.translate("Form", u"Seleccionar", None))
        self.opciones_CB.setItemText(1, QCoreApplication.translate("Form", u"Piedra", None))
        self.opciones_CB.setItemText(2, QCoreApplication.translate("Form", u"Papel", None))
        self.opciones_CB.setItemText(3, QCoreApplication.translate("Form", u"Tijeras", None))

        self.label_9.setText(QCoreApplication.translate("Form", u"P", None))
        self.cantELoc_LB.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"E", None))
        self.cantPLoc_LB.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Record total", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"G", None))
        self.cantGLoc_LB.setText(QCoreApplication.translate("Form", u"0", None))
        self.msjGame_LB.setText(QCoreApplication.translate("Form", u"Mensaje del juego", None))
        self.jugar_PB.setText(QCoreApplication.translate("Form", u"Jugar", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"P", None))
        self.cantGS_LB.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"E", None))
        self.cantPS_LB.setText(QCoreApplication.translate("Form", u"0", None))
        self.cantES_LB.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"G", None))
        self.msjSys_LB.setText(QCoreApplication.translate("Form", u"Mensaje de sistema", None))
#if QT_CONFIG(whatsthis)
        self.opcU2_LB.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.opcU2_LB.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Jugador 2", None))
        self.cerrar_PB.setText(QCoreApplication.translate("Form", u"Cerrar", None))
    # retranslateUi

