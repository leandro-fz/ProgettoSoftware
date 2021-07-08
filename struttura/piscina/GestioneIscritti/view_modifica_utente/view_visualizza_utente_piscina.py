from PyQt5.QtWidgets import QWidget, QLabel,QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QShortcut



class view_visualizza_utente_piscina(QWidget):

    def __init__(self, controllore_utente, parent=None):
        super(view_visualizza_utente_piscina, self).__init__(parent)

        self.controllore_utente = controllore_utente

        self.v_layout = QVBoxLayout()

        # labels contenenti dati del cliente
        self.create_label("Prenotante:         ", self.controllore_utente.get_nome_utente())

        self.h_layout = QHBoxLayout()

        self.create_button("Chiudi", self.mostra_indietro)

        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro)

        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

        self.setMinimumSize(500, 300)
        self.setMaximumSize(500, 300)
        self.setWindowTitle("Prenotazione Tennis")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/sfondotennissfocato.jpeg")
        sImage = oImage.scaled(QSize(500, 310))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    def create_label(self, testo, descrizione):
        h_layout = QHBoxLayout()

        label = QLabel(testo)
        label.setFont(QFont("Yu Gothic UI Light",15))
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