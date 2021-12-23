import sqlite3
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget

"""class HosgeldinEkrani(QDialog):
    def __init__(self):
        super(HosgeldinEkrani, self).__init__()
        loadUi("Hosgeldin.ui", self)
        self.giris.clicked.connect(self.gotogiris)
        self.hesapOlustur.clicked.connect(self.gotohesapOlustur)
        self.ileriButon.clicked.connect(self.hosgeldindenIleri)

    def gotohesapOlustur(self):
        olustur = HesapOlusturEkrani()
        widget.addWidget(olustur)
        widget.setCurrentIndex(widget.currentIndex()+1)



    def hosgeldindenIleri(self):
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotogiris(self):
        giris = GirisEkrani()
        widget.addWidget(giris)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.ileriButon.setEnabled(True)"""


class GirisEkrani(QDialog):
    def __init__(self):
        super(GirisEkrani, self).__init__()
        loadUi("Giris.ui", self)
        self.girisButon.clicked.connect(self.girisFonksiyonu)
        self.sifreGoster.stateChanged.connect(self.sifreyiGoster)
        self.geriButon.clicked.connect(self.giristenGeri)
        self.kayitOl.clicked.connect(self.gotoKayitOl)
        self.ileriButon.clicked.connect(self.giristenIleri)

    def giristenIleri(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoKayitOl(self):
        kayit = KayitOlEkrani()
        widget.addWidget(kayit)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.ileriButon.setEnabled(True)

    def sifreyiGoster(self):
        if self.sifreGoster.isChecked():
            self.sifreLine.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.sifreLine.setEchoMode(QtWidgets.QLineEdit.Password)

    def giristenGeri(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def girisFonksiyonu(self):
        email = self.epostaLine.text()
        sifre = self.sifreLine.text()
        conn = sqlite3.connect("deneme_data.db")
        cur = conn.cursor()
        #  cur.execute('INSERT INTO login_info (email, password) VALUES (?,?)', user_info)

        try:
            query2 = 'SELECT email FROM login_info WHERE email =\'' + email + "\'"

            cur.execute(query2)
            a = cur.fetchone()[0]
            print(a)
            print(query2)
        except Exception as e:
            print(e)
        query = 'SELECT password FROM login_info WHERE email =\'' + email + "\'"
        cur.execute(query)

        result_pass = cur.fetchone()[0]

        if result_pass == sifre:
            self.label_4.setText("Başarıyla giriş yapıldı")
            print("Başarıyla giriş yapıldı")
        else:
            self.label_4.setText("Geçersiz Şifre")


class KayitOlEkrani(QDialog):
    def __init__(self):
        super(KayitOlEkrani, self).__init__()
        loadUi("hesapolustur.ui", self)
        self.kayitOl.clicked.connect(self.kayitOlFonksiyon)
        self.geriButon.clicked.connect(self.kayittanGeri)
        self.sifreGoster.stateChanged.connect(self.sifreyiGoster)

    def kayitOlFonksiyon(self):
        email = self.epostaLine.text()
        sifre = self.sifreLine.text()
        sifreDogrula = self.sifreLine2.text()
        if sifre != sifreDogrula:
            self.hata.setText("Şifreler Eşleşmiyor!")
        else:

            conn = sqlite3.connect("deneme_data.db")
            cur = conn.cursor()
            kullanici = [email, sifre]
            cur.execute('INSERT INTO login_info (email,password) VALUES (?,?)', kullanici)
            conn.commit()
            conn.close()
            self.hata.setText("Kayıt Olma Başarılı")
            self.epostaLine.clear()
            self.sifreLine.clear()
            self.sifreLine2.clear()



    def sifreyiGoster(self):
        if self.sifreGoster.isChecked():
            self.sifreLine.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.sifreLine2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.sifreLine.setEchoMode(QtWidgets.QLineEdit.Password)
            self.sifreLine2.setEchoMode(QtWidgets.QLineEdit.Password)

    def kayittanGeri(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# main
app = QApplication(sys.argv)
welcome = GirisEkrani()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(1100)
widget.setFixedHeight(860)
widget.show()

try:
    pass
    sys.exit(app.exec_())
except:
    print("Exiting")
