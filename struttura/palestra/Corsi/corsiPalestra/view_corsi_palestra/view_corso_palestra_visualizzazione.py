from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QShortcut



#visualizzazione dettagli corso palestra
class view_corso_palestra_visualizzazione(QWidget):

    def __init__(self, controllore_corso_palestra, parent=None):
        super(view_corso_palestra_visualizzazione, self).__init__(parent)

        self.controllore_corso_palestra = controllore_corso_palestra

        self.v_layout = QVBoxLayout()
        #vari labels
        self.create_label("Giorno:        ", self.controllore_corso_palestra.get_giorno_corsiPalestra().strftime('%d/%m/%Y'))
        self.create_label("Orario:        ", self.controllore_corso_palestra.get_orario_premuto_corsiPalestra())
        self.create_label("Corso          ", self.controllore_corso_palestra.get_corso_Palestra())
        self.create_label("Istruttore          ", self.controllore_corso_palestra.get_istruttore_corsiPalestra())

        self.h_layout = QHBoxLayout()

        #pulsante chiudi
        self.create_button("Chiudi", self.mostra_indietro)

        self.shortcut_indietro = QShortcut(QKeySequence('Return'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro)

        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

        self.setMinimumSize(500, 300)
        self.setMaximumSize(500, 300)
        self.setWindowTitle("Corso Palestra")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(500, 310))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    #funzione per creare i label
    def create_label(self, testo, descrizione):
        h_layout = QHBoxLayout()

        label = QLabel(testo)
        label.setFont(QFont("Yu Gothic UI Light",15))
        h_layout.addWidget(label)


        label_di_testo = QLabel(descrizione)
        label_di_testo.setFont(QFont("Arial",15))
        h_layout.addWidget(label_di_testo)

        self.v_layout.addLayout(h_layout)

    #funzione per creare bottoni
    def create_button(self, titolo, funzione):
        bottone = QPushButton(titolo)
        bottone.setFont(QFont("Yu Gothic UI Light", 12))
        bottone.clicked.connect(funzione)
        self.h_layout.addWidget(bottone)
        bottone.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    #funzione per chiudere la pagina
    def mostra_indietro(self):
        self.close()