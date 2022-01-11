# import random
import sqlite3
# import string
import sys
import os
import re
from time import sleep

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import smtplib
from email.mime.text import MIMEText

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
        self.kayitOl.pressed.connect(self.kayitOlPressed)
        self.kayitOl.released.connect(self.kayitOlReleased)
        self.girisButon.pressed.connect(self.girisPressed)
        self.girisButon.released.connect(self.girisReleased)
        self.sifremiUnuttum.pressed.connect(self.sifremiUnuttumPressed)
        self.sifremiUnuttum.released.connect(self.sifremiUnuttumReleased)
        self.sifremiUnuttum.clicked.connect(self.sifreYenileme)

    # def giristenIleri(self):
    # widget.setCurrentIndex(widget.currentIndex() + 1)
    def girisPressed(self):
        self.girisButon.setStyleSheet("background-color: rgb(112, 174, 200);border-radius:20px;")

    def girisReleased(self):
        self.girisButon.setStyleSheet("background-color: rgb(143, 220, 255);border-radius:20px;")

    def sifremiUnuttumPressed(self):
        self.sifremiUnuttum.setStyleSheet("background-color: rgb(112, 174, 200);border-radius:20px;")

    def sifremiUnuttumReleased(self):
        self.sifremiUnuttum.setStyleSheet("background-color: rgb(143, 220, 255);border-radius:20px;")

    def kayitOlPressed(self):
        self.kayitOl.setStyleSheet("background-color: rgb(112, 174, 200);border-radius:20px;")

    def kayitOlReleased(self):
        self.kayitOl.setStyleSheet("background-color: rgb(143, 220, 255);border-radius:20px;")

    def sifreYenileme(self):
        ePosta = self.epostaLine.text()
        if not str(ePosta).endswith(".com"):
            self.label_4.setText("E-Postanizi Giriniz ")
        else:
            conn = sqlite3.connect("deneme_data.db")
            cur = conn.cursor()
            # lower = string.ascii_lowercase     # Random Sifre olusturmak icin
            # upper = string.ascii_uppercase
            # num = string.digits
            # all = lower+upper+num
            # temp = random.sample(all, 8)
            # sifre = "".join(temp)
            cur.execute('SELECT password FROM login_info WHERE email =\'' + ePosta + "\'")
            temp = cur.fetchone()
            if temp is None:
                self.label_4.setText("Kayitli E-Posta Bulunamadi")
            else:
                to = ePosta
                sender = 'MarmaraMusicPlayer@gmail.com'  # Mail gonderimi icin gmail hesabi olusturdum
                try:  # email= MarmaraMusicPlayer@gmail.com password= Marmara123
                    #  cur.execute('Update login_info set password = ? where email = ?', (sifre, ePosta)) # Databasedeki
                    #     conn.commit()                                    # şifre bilgisini yeni şifre ile degistiriyor
                    #     conn.close()
                    cur.execute(f'SELECT password FROM login_info WHERE email =\'' + ePosta + "\'")
                    sifre = cur.fetchone()[0]
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    password = 'Marmara123'
                    server.starttls()
                    server.login(sender, password)
                    message = MIMEText(f'Sifreniz: {sifre}')
                    message['Subject'] = 'Marmara Music Player Sifremi Unuttum'
                    message['From'] = sender
                    message['To'] = to
                    server.sendmail(sender, to, message.as_string())
                    self.label_4.setText("Sifreniz mailinize gonderildi.")
                    server.close()
                except Exception as e:
                    print(e)

    def gotoMusicPlayer(self):
        try:
            well = Mp3Player()
            widget.addWidget(well)
            widget.show()
        except Exception as e:
            print(e)

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
        kayit = KayitOlEkrani()
        widget.addWidget(kayit)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def girisFonksiyonu(self):
        email = self.epostaLine.text()
        global Gemail
        Gemail = email
        sifre = self.sifreLine.text()
        conn = sqlite3.connect("deneme_data.db")
        cur = conn.cursor()
        #  cur.execute('INSERT INTO login_info (email, password) VALUES (?,?)', user_info)
        query = 'SELECT password FROM login_info WHERE email =\'' + email + "\'"
        cur.execute(query)

        result_pass = cur.fetchone()[0]

        if result_pass == sifre:
            mp3Player = Mp3Player()
            widget.addWidget(mp3Player)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.label_4.setText("Başarıyla giriş yapıldı")
            # self.gotoMusicPlayer()
        else:
            self.label_4.setText("Geçersiz Şifre")
        conn.close()


class KayitOlEkrani(QDialog):
    def __init__(self):
        super(KayitOlEkrani, self).__init__()
        loadUi("hesapolustur.ui", self)
        self.kayitOl.clicked.connect(self.kayitOlFonksiyon)
        self.geriButon.clicked.connect(self.kayittanGeri)
        self.sifreGoster.stateChanged.connect(self.sifreyiGoster)
        self.kayitOl.pressed.connect(self.kayitOlPressed)
        self.kayitOl.released.connect(self.kayitOlReleased)

    def kayitOlPressed(self):
        self.kayitOl.setStyleSheet("background-color: rgb(112, 174, 200);border-radius:20px;")

    def kayitOlReleased(self):
        self.kayitOl.setStyleSheet("background-color: rgb(143, 220, 255);border-radius:20px;")

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
        giris = GirisEkrani()
        widget.addWidget(giris)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()


class Mp3Player(QDialog):
    def __init__(self):
        super(Mp3Player, self).__init__()
        self.sarki = None
        loadUi("Mp3Player.ui", self)
        self.timer = QTimer()
        # timer.deleteLater()
        # self.timer.singleShot(10, self.InfoLabel)
        self.position = 0
        self.durum = 0
        self.anlikSarki = ""
        self.index = None
        self.mute = 0
        self.sarkilar = []
        self.favoriDurumu = 0
        
     
        
        # self.sarkigeriButon.pressed.connect(self.sarkigeriBasili)
        # self.durdurButon.pressed.connect(self.durdurBasili)
        # self.oynatButon.pressed.connect(self.oynatBasili)
        # self.duraklatButon.pressed.connect(self.duraklatBasili)
        # self.sarkileriButon.pressed.connect(self.sarkileriBasili)
        # self.begenButon.pressed.connect(self.begenBasili)

        self.sarkiYolu.clicked.connect(self.sarkiYoluAra)
        self.cikisButton.clicked.connect(self.showPopUp)
        self.oynatButon.clicked.connect(self.sarkiOynat)
        self.duraklatButon.clicked.connect(self.sarkiDuraklat)
        self.sarkigeriButon.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.durdurButon.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.oynatButon.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.duraklatButon.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.sarkileriButon.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))
        self.sarkiYolu.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))
        self.sarkigeriSar.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekBackward))
        self.sarkileriSar.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))
        self.muteButon.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        #  self.begenButon.setIcon(QIcon("begen.png"))
        #  self.begenmeButon.setIcon(QIcon("begenme.png"))

        self.oynatButon.setEnabled(False)
        self.oynatButon.setStyleSheet("background-color : rgb(79,79,79);}")

        self.player = QMediaPlayer()
        self.sarkiKonumu.setRange(0, 0)
        self.sarkiKonumu.sliderMoved.connect(self.set_position)
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.sarkileriSar.clicked.connect(self.sarkiIleriSar)
        self.sarkigeriSar.clicked.connect(self.sarkiGeriSar)
        self.sarkigeriButon.clicked.connect(self.sarkiGeri)
        self.sarkileriButon.clicked.connect(self.sarkiIleri)
        self.durdurButon.clicked.connect(self.sarkiDurdur)
        self.sarkiListesi.doubleClicked.connect(self.sarkiOynat)
        self.sesSeviyesi.valueChanged.connect(self.sesDegis)
        self.muteButon.clicked.connect(self.muteDegis)
        self.sarkiKonumu.sliderPressed.connect(self.sliderPressed)
        self.sarkiKonumu.sliderReleased.connect(self.sliderReleased)
        self.begenButon.clicked.connect(self.favoriEkle)
        self.begenButon.pressed.connect(self.begenButonPressed)
        self.begenButon.released.connect(self.begenButonReleased)
        self.begenmeButon.pressed.connect(self.begenmeButonPressed)
        self.begenmeButon.released.connect(self.begenmeButonReleased)
        self.begenmeButon.clicked.connect(self.favoriSil)
        self.favorilerButon.clicked.connect(self.favoriGosterGizle)
        
        # ses = self.player.volume()
        self.sesSeviyesi.setRange(0, 100)
        self.sesSeviyesi.setValue(50)

        self.setGeometry(35, 100, 1000, 800)

        conn = sqlite3.connect("deneme_data.db")
        cur = conn.cursor()
        query = "SELECT sarki_yolu FROM sarkilar WHERE email =\'" + Gemail + "\'"
        cur.execute(query)
        self.sarkilar = cur.fetchall()
        for i in range(len(self.sarkilar)):
            temp = self.sarkilar[i][0]
            self.sarkilar[i] = temp
            self.sarkiListesi.addItems(re.findall("/.+/(.+)\.mp3", self.sarkilar[i]))
        conn.close()
        

    def begenmeButonPressed(self):
        self.begenmeButon.setStyleSheet("background-color: rgb(70, 70, 70);border-radius:20px;")

    def begenmeButonReleased(self):
        self.begenmeButon.setStyleSheet("background-color: rgb(112, 112, 112);border-radius:20px;")

    def begenButonPressed(self):
        self.begenButon.setStyleSheet("background-color: rgb(70, 70, 70);border-radius:20px;")

    def begenButonReleased(self):
        self.begenButon.setStyleSheet("background-color: rgb(112, 112, 112);border-radius:20px;")


    def showPopUp(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowIcon(QIcon("mp3Player.png"))
        msg.setWindowTitle("Cikis")
        msg.setText("Cikmak istediginizden emin misiniz?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        a = msg.exec()
        if a == QMessageBox.Yes:
            self.sarkiDurdur()
            welll = GirisEkrani()
            widget.addWidget(welll)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            widget.show()
        elif a == QMessageBox.No:
            pass

    # def gotoCikis(self):
    #     try:
    #         self.showPopUp()
    #         # self.sarkiDurdur()
    #         # welll = GirisEkrani()
    #         # widget.addWidget(welll)
    #         # widget.setCurrentIndex(widget.currentIndex()+1)
    #         # widget.show()
    #     except Exception as e:
    #         print(e)

    def sliderPressed(self):
        self.player.setMuted(1)

    def sliderReleased(self):
        self.player.setMuted(0)

    def sarkiDuraklat(self):
        self.player.pause()

    def sarkiIleriSar(self):
        self.player.setPosition(int(self.player.position()) + 2000)

    def sarkiGeriSar(self):
        self.player.setPosition(int(self.player.position()) - 2000)

    def sarkiIleri(self):
        self.durum = 1
        try:
            self.sarkiListesi.setCurrentRow(self.index + 1)
            self.sarkiOynat()
        except:
            pass

    def sarkiGeri(self):
        self.durum = 1
        try:
            self.sarkiListesi.setCurrentRow(self.index - 1)
            self.sarkiOynat()
        except:
            pass

    def sarkiYoluAra(self):
        dosyayolu = QFileDialog()
        dosyayolu.setFileMode(QFileDialog.ExistingFiles)
        isimler = dosyayolu.getOpenFileNames(self, "Dosyaları Aç", os.getenv("Home"), "Müzik Dosyası (*.mp3) ")
        self.sarki = isimler[0]
        conn = sqlite3.connect("deneme_data.db")
        cur = conn.cursor()
        for i in range(len(self.sarki)):
            veri = ["", "", 0]
            veri[0] = Gemail
            veri[1] = self.sarki[i]
            cur.execute('INSERT INTO sarkilar (email,sarki_yolu,favori) VALUES (?,?,?)', veri)
            self.sarkilar.append(self.sarki[i])
            self.sarkiListesi.addItems(re.findall("/.+/(.+)\.mp3", self.sarki[i]))
        if len(isimler[0]) > 0:
            self.oynatButon.setEnabled(True)
            self.oynatButon.setStyleSheet("background-color : rgb(112, 112, 112);}")
        conn.commit()
        conn.close()

    def sarkiOynat(self):
        if self.durum == 0:
            if self.anlikSarki != self.sarkilar[self.sarkiListesi.currentRow()]:
                sarkiYolu = self.sarkilar[self.sarkiListesi.currentRow()]
                self.anlikSarki = sarkiYolu
                self.index = self.sarkiListesi.currentRow().__index__()
                url = QUrl.fromLocalFile(sarkiYolu)
                content = QMediaContent(url)
                self.player.setMedia(content)
                self.player.play()
                self.durum = 1
            else:
                self.player.play()
        else:
            if self.anlikSarki != self.sarkilar[self.sarkiListesi.currentRow()]:
                sarkiYolu = self.sarkilar[self.sarkiListesi.currentRow()]
                self.anlikSarki = sarkiYolu
                self.index = self.sarkiListesi.currentRow().__index__()
                url = QUrl.fromLocalFile(sarkiYolu)
                content = QMediaContent(url)
                self.player.setMedia(content)
                self.player.play()
                # self.durum = 1
            else:
                self.player.play()
        liste = re.findall("/.+/(.+)\.mp3", self.anlikSarki)
        self.sarkiAdi.setText(liste[len(liste) - 1])

    def sarkiDurdur(self):
        self.durum = 0
        self.player.stop()
        self.sarkiKonumu.setValue(0)

    def muteDegis(self):
        if self.mute == 0:
            self.mute = 1
            self.player.setMuted(1)
            self.muteButon.setIcon(self.style().standardIcon(QStyle.SP_MediaVolumeMuted))
        else:
            self.mute = 0
            self.player.setMuted(0)
            self.muteButon.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))

    def set_position(self, position):
        self.player.setPosition(position)

    def position_changed(self, position):
        self.sarkiKonumu.setValue(position)
        duration = self.player.duration()
        value = self.sarkiKonumu.value()
        if value == duration:
            self.sarkiOynat()

    def duration_changed(self, duration):
        self.sarkiKonumu.setRange(0, duration)

    def sesDegis(self):
        ses = self.sesSeviyesi.value()
        self.player.setVolume(ses)
        self.sesSeviye.setText("%" + str(ses))

    def favoriEkle(self):
        conn = sqlite3.connect("deneme_data.db")
        cur = conn.cursor()
        yol = self.sarkilar[self.sarkiListesi.currentRow()]
        cur.execute('UPDATE sarkilar SET favori=\'1\' WHERE sarki_yolu=\'' + yol + "\'")
        a = re.findall(".+/(.+)\.mp3", yol)
        self.InfoLabel.setText(f'{a[0]} favorilere eklendi')
        conn.commit()
        conn.close()

    def favoriSil(self):
        conn = sqlite3.connect("deneme_data.db")
        cur = conn.cursor()
        yol = self.sarkilar[self.sarkiListesi.currentRow()]
        cur.execute('UPDATE sarkilar SET favori=\'0\' WHERE sarki_yolu=\'' + yol + "\'")
        a = re.findall(".+/(.+)\.mp3", yol)
        self.InfoLabel.setText(f'{a[0]} favorilerden cikartildi')
        conn.commit()
        conn.close()
        self.favoriDurumu = 0
        self.favoriGosterGizle()

    def favoriGosterGizle(self):
        if self.favoriDurumu == 0:
            self.sarkiListesi.clear()
            self.sarkilar.clear()
            self.favorilerButon.setText("Favorileri Gizle")
            conn = sqlite3.connect("deneme_data.db")
            cur = conn.cursor()
            query = 'SELECT favori,sarki_yolu FROM sarkilar WHERE email =\'' + Gemail + '\''
            cur.execute(query)
            temp = cur.fetchall()
            favorite = []
            songs = []
            for i in range(len(temp)):
                favorite.append(temp[i][0])
                songs.append(temp[i][1])
            conn.close()
            for i in range(len(songs)):
                if favorite[i] == 1:
                    self.sarkilar.append(songs[i])
                    self.sarkiListesi.addItems(re.findall("/.+/(.+)\.mp3", songs[i]))

            self.favoriDurumu = 1
        else:
            self.sarkiListesi.clear()
            self.sarkilar.clear()
            self.favorilerButon.setText("Favorileri Goster")
            conn = sqlite3.connect("deneme_data.db")
            cur = conn.cursor()
            query = "SELECT sarki_yolu FROM sarkilar WHERE email =\'" + Gemail + "\'"
            cur.execute(query)
            self.sarkilar = cur.fetchall()
            for i in range(len(self.sarkilar)):
                temp = self.sarkilar[i][0]
                self.sarkilar[i] = temp
                self.sarkiListesi.addItems(re.findall("/.+/(.+)\.mp3", self.sarkilar[i]))
                conn.close()
            self.favoriDurumu = 0


# main
app = QApplication(sys.argv)

welcome = GirisEkrani()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(1100)
widget.setFixedHeight(860)
widget.setWindowTitle("Mp3 Player")
widget.setWindowIcon(QIcon("mp3Player.png"))
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
