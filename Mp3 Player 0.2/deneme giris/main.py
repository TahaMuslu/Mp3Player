import random
import sqlite3
import string
import sys
import os
import re
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaContent,QMediaPlayer 
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
        self.ileriButon.clicked.connect(self.giristenIleri)
        self.sifremiUnuttum.clicked.connect(self.sifreYenileme)

    def giristenIleri(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
                sender = 'MarmaraMusicPlayer@gmail.com' # Mail gonderimi icin gmail hesabi olusturdum
                try:                          # email= MarmaraMusicPlayer@gmail.com password= Marmara123
               #     cur.execute('Update login_info set password = ? where email = ?', (sifre, ePosta)) # Databasedeki
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
        query = 'SELECT password FROM login_info WHERE email =\'' + email + "\'"
        cur.execute(query)

        result_pass = cur.fetchone()[0]

        if result_pass == sifre:
            mp3Player = Mp3Player()
            widget.addWidget(mp3Player)
            widget.setCurrentIndex(widget.currentIndex()+1)
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


class Mp3Player(QDialog):
    def __init__(self):
        super(Mp3Player, self).__init__()
        loadUi("Mp3Player.ui", self)
        self.setWindowTitle("dgdsg")
        self.setWindowIcon(QIcon("mp3Player.png"))
                
        self.position = 0
        self.durum = 0
        self.anlikSarki=""
        self.index=""
        self.mute=0
        
        # self.sarkigeriButon.pressed.connect(self.sarkigeriBasili)
        # self.durdurButon.pressed.connect(self.durdurBasili)
        # self.oynatButon.pressed.connect(self.oynatBasili)
        # self.duraklatButon.pressed.connect(self.duraklatBasili)
        # self.sarkileriButon.pressed.connect(self.sarkileriBasili)
        # self.begenButon.pressed.connect(self.begenBasili)
        self.sarkiYolu.clicked.connect(self.sarkiYoluAra)
        
        
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
        self.begenButon.setIcon(QIcon("begen.png"))
        
        
        
        self.oynatButon.setEnabled(False)
        self.oynatButon.setStyleSheet("background-color : rgb(79,79,79);}")

        
        self.player = QMediaPlayer()
        self.sarkiKonumu.setRange(0,0)
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
        
        ses = self.player.volume()
        self.sesSeviyesi.setRange(0,100)
        self.sesSeviyesi.setValue(int(ses)/2)
        
        self.setGeometry(35,100,1000,800)
        
        
    # def sarkigeriBasili(self):
    #     self.sarkigeriButon.setStyleSheet("QPushButton::pressed{border: 1px solid white;background-color : rgb(79,79,79);color: rgb(225, 225, 225);}")
        
    # def durdurBasili(self):
    #     self.durdurButon.setStyleSheet("QPushButton::pressed{border: 1px solid white;background-color : rgb(79,79,79);color: rgb(225, 225, 225);}")
 
    # def oynatBasili(self):
    #     self.oynatButon.setStyleSheet("QPushButton::pressed{border: 1px solid white;background-color : rgb(79,79,79);color: rgb(225, 225, 225);}")
 
    # def duraklatBasili(self):
    #     self.duraklatButon.setStyleSheet("QPushButton::pressed{border: 1px solid white;background-color : rgb(79,79,79);color: rgb(225, 225, 225);}")
 
    # def sarkileriBasili(self):
    #     self.sarkileriButon.setStyleSheet("QPushButton::pressed{border: 1px solid white;background-color : rgb(79,79,79);color: rgb(225, 225, 225);}")
   
    # def begenBasili(self):
    #      self.begenButon.setStyleSheet("QPushButton::pressed{border: 1px solid white;background-color : rgb(79,79,79);color: rgb(225, 225, 225);}")
        
         
        
    def sarkiDuraklat(self):
        self.player.pause()
        
    
    def sarkiIleriSar(self):
        self.player.setPosition(int(self.player.position()) + 2000)
    
    def sarkiGeriSar(self):
        self.player.setPosition(int(self.player.position()) - 2000)
        
        
    def sarkiIleri(self):
        self.durum=1
        try:  
            self.sarkiListesi.setCurrentRow(self.index + 1)
            self.sarkiOynat()
        except:
            pass
        
    def sarkiGeri(self):
        self.durum=1
        try:
            self.sarkiListesi.setCurrentRow(self.index - 1)
            self.sarkiOynat()
        except:
            pass
    
    
    def sarkiYoluAra(self):
        dosyayolu = QFileDialog()
        dosyayolu.setFileMode(QFileDialog.ExistingFiles)
        isimler = dosyayolu.getOpenFileNames(self,"Dosyaları Aç",os.getenv("Home"))
        self.sarki = isimler[0]
        self.sarkiListesi.addItems(self.sarki)
        if len(isimler[0])>0:
            self.oynatButon.setEnabled(True)
            self.oynatButon.setStyleSheet("background-color : rgb(112, 112, 112);}")
        
        
    def sarkiOynat(self):
        if self.durum==0:
            if self.anlikSarki!=self.sarkiListesi.currentItem().text():
                sarkiYolu = self.sarkiListesi.currentItem().text()
                self.anlikSarki=sarkiYolu
                self.index=self.sarkiListesi.currentRow().__index__()
                url = QUrl.fromLocalFile(sarkiYolu)
                content = QMediaContent(url)
                self.player.setMedia(content)
                self.player.play()
                self.durum = 1
            else:
                self.player.play()
        else:
            if self.anlikSarki!=self.sarkiListesi.currentItem().text():
                sarkiYolu = self.sarkiListesi.currentItem().text()
                self.anlikSarki=sarkiYolu
                self.index=self.sarkiListesi.currentRow().__index__()
                url = QUrl.fromLocalFile(sarkiYolu)
                content = QMediaContent(url)
                self.player.setMedia(content)
                self.player.play()
                self.durum = 1
            else:
                self.player.play()
        liste=re.findall("/.+/(.+)\.mp3", self.anlikSarki)
        self.sarkiAdi.setText(liste[len(liste)-1])
            
    def sarkiDurdur(self):
        self.durum=0
        self.player.stop()
        self.sarkiKonumu.setValue(0)
        
    def muteDegis(self):
        if self.mute==0:
            self.mute=1
            self.player.setMuted(1)
            self.muteButon.setIcon(self.style().standardIcon(QStyle.SP_MediaVolumeMuted))
        else:
            self.mute=0
            self.player.setMuted(0)
            self.muteButon.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
            

    def set_position(self,position):
        self.player.setPosition(position)

    def position_changed(self,position):
        self.sarkiKonumu.setValue(position)
        duration = self.player.duration()
        value=self.sarkiKonumu.value()
        if value==duration:
            self.sarkiOynat()

    def duration_changed(self,duration):
        self.sarkiKonumu.setRange(0,duration)
        
    def sesDegis(self):
        ses=self.sesSeviyesi.value()
        self.player.setVolume(ses)
        self.sesSeviye.setText("%"+str(ses))




# main
app = QApplication(sys.argv)
welcome = Mp3Player()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(1100)
widget.setFixedHeight(860)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
    Mp3Player().player.disconnect()
    