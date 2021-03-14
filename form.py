import sys  
import sqlite3
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout,QLineEdit,QCheckBox,QHBoxLayout,QTextEdit
from PyQt5.QtCore import Qt 
from PyQt5 import QtWidgets,QtGui


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def baglanti_olustur(self):
        baglanti = sqlite3.connect("data.db") 
        self.cursor = baglanti.cursor()

        self.cursor.execute("Create Table If not exists basvuranlar (ad TEXT, soyad TEXT, email TEXT, meslek TEXT, gorus TEXT)")

        baglanti.commit()

    def init_ui(self):
        self.company_page = QLabel()
        self.company_page.setPixmap(QtGui.QPixmap("aai.png"))
        self.ad = QLabel("Ad:")
        self.ad_yaziALani = QLineEdit()
        self.soyad = QLabel("Soyad:")
        self.soyad_yaziAlani = QLineEdit()
        self.email = QLabel("E-Posta:")
        self.email_yaziAlani = QLineEdit()
        self.meslek = QLabel("Meslek:")
        self.meslek_yaziAlani = QLineEdit()
        self.soru = QLabel("Hangi Yazılım Dilinde Profesyonelsiniz?")
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.cdili = QRadioButton("C and C++")
        self.csharp = QRadioButton("C#")
        self.html = QRadioButton("HTML5")
        self.css = QRadioButton("CSS3")
        self.js = QRadioButton("JavaScript")
        self.bootstrap = QRadioButton("Bootstrap 4")
        self.swift = QRadioButton("Swift UI")
        self.kotlin = QRadioButton("Kotlin")
        self.perl = QRadioButton("Perl")
        self.dart = QRadioButton("Dart")
        self.flutter = QRadioButton("Flutter")
        self.php = QRadioButton("PHP")
        self.diger = QRadioButton("Diğer")
        self.gorus = QLabel("Bize Kendinizden Bahseder Misiniz?")
        self.gorus_yaziAlani = QTextEdit()
        self.temizle = QPushButton("Metni Temizle")
        self.kosullar = QCheckBox("Sözleşmeyi Okudum ve Kabul Ediyorum")
        self.kosullar_yaziAlani = QLabel("")
        self.gonder = QPushButton("Gönder")
        self.geriBildirim = QLabel("")
        self.yazilim = QLabel("from Alper Aybak")
        self.yazilim.setAlignment(Qt.AlignCenter) 
        self.labelInfo = QLabel()
        

        v_box = QVBoxLayout()
        v_box.addWidget(self.company_page)


        v_box.addStretch()
        v_box.addStretch()
        v_box.addWidget(self.ad)
        v_box.addWidget(self.ad_yaziALani)
        v_box.addWidget(self.soyad)
        v_box.addWidget(self.soyad_yaziAlani)
        v_box.addWidget(self.email)
        v_box.addWidget(self.email_yaziAlani)
        v_box.addWidget(self.meslek)
        v_box.addWidget(self.meslek_yaziAlani)
        v_box.addWidget(self.soru)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.cdili)
        v_box.addWidget(self.csharp)
        v_box.addWidget(self.html)
        v_box.addWidget(self.css)
        v_box.addWidget(self.js)
        v_box.addWidget(self.bootstrap)
        v_box.addWidget(self.swift)
        v_box.addWidget(self.kotlin)
        v_box.addWidget(self.perl)
        v_box.addWidget(self.dart)
        v_box.addWidget(self.flutter)
        v_box.addWidget(self.php)
        v_box.addWidget(self.diger)
        v_box.addWidget(self.labelInfo)
        v_box.addStretch()
        v_box.addStretch()
        v_box.addWidget(self.gorus)
        v_box.addWidget(self.gorus_yaziAlani)
        v_box.addWidget(self.temizle)
        v_box.addStretch()
        v_box.addStretch()
        v_box.addWidget(self.kosullar)
        v_box.addWidget(self.kosullar_yaziAlani)
        v_box.addWidget(self.gonder)
        v_box.addStretch()
        v_box.addStretch()
        v_box.addWidget(self.geriBildirim)
        v_box.addWidget(self.yazilim)


        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("AAI_Company.exe")
        self.temizle.clicked.connect(self.click_temizle)
        self.gonder.clicked.connect(self.click_gonder)
        self.kosullar.clicked.connect(lambda: self.click_sozlesme(self.kosullar.isChecked(),self.kosullar_yaziAlani))

        self.java.toggled.connect(self.toggleRadio)
        self.python.toggled.connect(self.toggleRadio)
        self.cdili.toggled.connect(self.toggleRadio)
        self.csharp.toggled.connect(self.toggleRadio)
        self.html.toggled.connect(self.toggleRadio)
        self.css.toggled.connect(self.toggleRadio)
        self.js.toggled.connect(self.toggleRadio)
        self.bootstrap.toggled.connect(self.toggleRadio)
        self.swift.toggled.connect(self.toggleRadio)
        self.kotlin.toggled.connect(self.toggleRadio)
        self.perl.toggled.connect(self.toggleRadio)
        self.dart.toggled.connect(self.toggleRadio)
        self.flutter.toggled.connect(self.toggleRadio)
        self.php.toggled.connect(self.toggleRadio)
        self.diger.toggled.connect(self.toggleRadio)
        self.show()

    def click_temizle(self):
        self.gorus_yaziAlani.clear()

    def click_gonder(self):
        self.geriBildirim.setText("İlginiz İçin Teşekkür Ederiz.\nBiz Size Geri Dönüş Yapacağız...")

    def click_sozlesme(self,kosullar,yazi_alani):
        if kosullar:
            yazi_alani.setText("Sözleşmeyi Kabul Ettiniz.")
        else:
            yazi_alani.setText("Sözleşmeyi Onaylamadınız!")

    def toggleRadio(self):
        rdButon = self.sender()
        if rdButon.isChecked():
            self.labelInfo.setText("Seçimininz  : " + rdButon.text())
        else:
            self.labelInfo.setText("Seçimininz  : ")





app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())