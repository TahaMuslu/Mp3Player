# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/90552/Desktop/qtdesign/qt_designer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 640)
        MainWindow.setMinimumSize(QtCore.QSize(510, 640))
        MainWindow.setMaximumSize(QtCore.QSize(510, 640))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#centralwidget{\n"
"background-image: url(:/iconss/icons/512x512bb.jpg);\n"
"}")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 350, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 380, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.epostaLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.epostaLineEdit.setGeometry(QtCore.QRect(220, 350, 151, 21))
        self.epostaLineEdit.setObjectName("epostaLineEdit")
        self.kayitOl = QtWidgets.QPushButton(self.centralwidget)
        self.kayitOl.setGeometry(QtCore.QRect(250, 500, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kayitOl.sizePolicy().hasHeightForWidth())
        self.kayitOl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.kayitOl.setFont(font)
        self.kayitOl.setAutoFillBackground(False)
        self.kayitOl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.732773, x2:1, y2:0, stop:0.373134 rgba(249,107,68,255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 5px;\n"
"")
        self.kayitOl.setObjectName("kayitOl")
        self.girisYap = QtWidgets.QPushButton(self.centralwidget)
        self.girisYap.setGeometry(QtCore.QRect(240, 430, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.girisYap.sizePolicy().hasHeightForWidth())
        self.girisYap.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.girisYap.setFont(font)
        self.girisYap.setAutoFillBackground(False)
        self.girisYap.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.732773, x2:1, y2:0, stop:0.373134 rgba(249,107,68,255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 5px;\n"
"")
        self.girisYap.setObjectName("girisYap")
        self.sifremiUnuttum = QtWidgets.QPushButton(self.centralwidget)
        self.sifremiUnuttum.setGeometry(QtCore.QRect(98, 430, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sifremiUnuttum.sizePolicy().hasHeightForWidth())
        self.sifremiUnuttum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sifremiUnuttum.setFont(font)
        self.sifremiUnuttum.setAutoFillBackground(False)
        self.sifremiUnuttum.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.732773, x2:1, y2:0, stop:0.373134 rgba(249,107,68,255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 5px;\n"
"")
        self.sifremiUnuttum.setObjectName("sifremiUnuttum")
        self.sifreLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sifreLineEdit.setGeometry(QtCore.QRect(220, 380, 151, 21))
        self.sifreLineEdit.setObjectName("sifreLineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 460, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 540, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 26))
        self.menubar.setObjectName("menubar")
        self.menuX = QtWidgets.QMenu(self.menubar)
        self.menuX.setObjectName("menuX")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionA = QtWidgets.QAction(MainWindow)
        self.actionA.setObjectName("actionA")
        self.menuX.addAction(self.actionA)
        self.menubar.addAction(self.menuX.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Player"))
        self.label.setText(_translate("MainWindow", "E-Posta:"))
        self.label_2.setText(_translate("MainWindow", "Şifre:"))
        self.kayitOl.setText(_translate("MainWindow", "Kayıt Ol"))
        self.girisYap.setText(_translate("MainWindow", "Giriş Yap"))
        self.sifremiUnuttum.setText(_translate("MainWindow", "Şifremi Unuttum"))
        self.label_4.setText(_translate("MainWindow", "Hesabın yok mu?"))
        self.menuX.setTitle(_translate("MainWindow", "Dosya"))
        self.actionA.setText(_translate("MainWindow", "Çıkış Yap"))
        self.actionA.setShortcut(_translate("MainWindow", "Esc"))

# import icons_rc
# import iconss_rc