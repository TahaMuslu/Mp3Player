import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from qt_designer_python import Ui_MainWindow
from PyQt5.uic import loadUi

class music(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sifreLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        
    @pyqtSlot()
    def on_kayitOl_clicked(self):
        self.ui.label_3.setText("Kayit Olma islemi")

    @pyqtSlot()
    def on_sifremiUnuttum_clicked(self):
        self.ui.label_3.setText("Sifre Yenileme islemi")

    @pyqtSlot()
    def on_girisYap_clicked(self):
        email = self.ui.epostaLineEdit.text()
        sifre = self.ui.sifreLineEdit.text()
        print("Basariyla giris yapildi.\tEmail:", email, "sifre:",sifre)
        self.ui.label_3.setText("Giris Yapma islemi")

    @pyqtSlot()                 # Sol ustteki dosya menu barindan cikis yapma islemi
    def on_actionA_triggered(self):
        widget.close()
        
        
        
        
                                # Pressed-released fonksiyonlarinda
    @pyqtSlot()                 # Mouse butona tiklarken butonun arkaplaninin rengi degisiyor butonu birakinca eski haline donuyor
    def on_sifremiUnuttum_pressed(self):
        self.ui.sifremiUnuttum.setStyleSheet("background-color: rgb(255, 60, 35);border-radius:5px;")

    @pyqtSlot()                             
    def on_sifremiUnuttum_released(self):
        self.ui.sifremiUnuttum.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.568, x2:1, y2:0, stop:0 rgba(249,107,68,255), stop:1 rgba(255, 255, 255, 255));border-radius:5px;")
    
    @pyqtSlot()
    def on_kayitOl_pressed(self):
        self.ui.kayitOl.setStyleSheet("background-color: rgb(255, 60, 35);border-radius:5px;")
    
    @pyqtSlot()
    def on_kayitOl_released(self):
        self.ui.kayitOl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.568, x2:1, y2:0, stop:0 rgba(249,107,68,255), stop:1 rgba(255, 255, 255, 255));border-radius:5px;")
    
    @pyqtSlot()
    def on_girisYap_pressed(self):
        self.ui.girisYap.setStyleSheet("background-color: rgb(255, 60, 35);border-radius:5px;")
    
    @pyqtSlot()
    def on_girisYap_released(self):
        self.ui.girisYap.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.568, x2:1, y2:0, stop:0 rgba(249,107,68,255), stop:1 rgba(255, 255, 255, 255));border-radius:5px;")




app = QApplication(sys.argv)
mainwindow = music()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(510)
widget.setFixedHeight(640)

widget.show()
app.exec_()