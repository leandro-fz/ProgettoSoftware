from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QShortcut




class view_corso_piscina_visualizzazione(QWidget):

    def __init__(self, controllore_corso_piscina, parent=None):
        super(view_corso_piscina_visualizzazione, self).__init__(parent)

        self.controllore_corso_piscina = controllore_corso_piscina

        self.v_layout = QVBoxLayout()

        self.create_label("Giorno:        ", self.controllore_corso_piscina.get_giorno__corsiPiscina().strftime('%d/%m/%Y'))
        self.create_label("Orario:        ", self.controllore_corso_piscina.get_orario_premuto_corsiPiscina())
        self.create_label("Corso          ", self.controllore_corso_piscina.get_corso_Piscina())
        self.create_label("Istruttore          ", self.controllore_corso_piscina.get_istruttore_corsiPiscina())

        self.h_layout = QHBoxLayout()

        self.create_button("Chiudi", self.mostra_indietro)

        self.shortcut_indietro = QShortcut(QKeySequence('Return'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro)

        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

        self.setMinimumSize(500, 300)
        self.setMaximumSize(500, 300)
        self.setWindowTitle("Corso Nuoto")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/piscina-sfondo_foto.jpg")
        sImage = oImage.scaled(QSize(500, 310))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    def create_label(self, testo, descrizione):
        h_layout = QHBoxLayout()

        label = QLabel(testo)
        label.setFont(QFont("Arial",15))
        h_layout.addWidget(label)


        label_di_testo = QLabel(descrizione)
        label_di_testo.setFont(QFont("Arial",15))
        h_layout.addWidget(label_di_testo)

        self.v_layout.addLayout(h_layout)

    def create_button(self, titolo, funzione):
        bottone = QPushButton(titolo)
        bottone.setFont(QFont("Yu Gothic UI Light", 12))
        bottone.clicked.connect(funzione)
        self.h_layout.addWidget(bottone)
        bottone.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def mostra_indietro(self):
        self.close()