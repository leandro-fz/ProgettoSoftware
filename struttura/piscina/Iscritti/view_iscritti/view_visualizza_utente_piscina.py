from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QShortcut

from gestione.cliente.certificati.controller_certificati.controller_certficati import controller_certificati


class view_visualizza_utente_piscina(QWidget):

    def __init__(self, controllore_abbonamento, parent=None):
        super(view_visualizza_utente_piscina, self).__init__(parent)

        self.controllore_abbonamento = controllore_abbonamento
        self.controllore_certificato = controller_certificati()

        self.v_layout = QVBoxLayout()

        # labels contenenti dati del cliente
        self.create_label("Nome:        ", self.controllore_abbonamento.get_nome_abbonamento())
        self.create_label("Cognome:         ", self.controllore_abbonamento.get_cognome_abbonamento())
        self.create_label("Codice fiscale:         ", self.controllore_abbonamento.get_codicefiscale_abbonamento())
        self.create_label("Nato a:            ", self.controllore_abbonamento.get_nato_abbonamento())
        self.create_label("Data di nascita:        ", self.controllore_abbonamento.get_data_abbonamento().strftime('%d/%m/%Y'))
        self.create_label("Residenza:            ", self.controllore_abbonamento.get_residenza_abbonamento())
        self.create_label("Email:            ", self.controllore_abbonamento.get_email_abbonamento())
        self.create_label("Cellulare:            ", str(self.controllore_abbonamento.get_cellulare_abbonamento()))
        self.create_label("Struttura:            ", self.controllore_abbonamento.get_struttura_abbonamento())
        self.create_label("Abbonamento:            ", self.controllore_abbonamento.get_tipoabbonamento_abbonamento())
        self.create_label("Certificato valido fino al:            ", self.controllore_certificato.get_certificato_by_codicefiscale(self.controllore_abbonamento.get_codicefiscale_abbonamento()).datafine.strftime('%d/%m/%Y'))
        self.create_label("Scadenza abbonamento:            ", self.controllore_abbonamento.get_scadenza_abbonamento(self.controllore_abbonamento.get_tipoabbonamento_abbonamento()).strftime('%d/%m/%Y'))



        self.h_layout = QHBoxLayout()

        self.create_button("Chiudi", self.mostra_indietro)

        self.shortcut_indietro = QShortcut(QKeySequence('Return'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro)

        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

        self.setMinimumSize(700, 600)
        self.setMaximumSize(700, 600)
        self.setWindowTitle("Utente piscina")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/piscina-sfondo_foto.jpg")
        sImage = oImage.scaled(QSize(700, 600))
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