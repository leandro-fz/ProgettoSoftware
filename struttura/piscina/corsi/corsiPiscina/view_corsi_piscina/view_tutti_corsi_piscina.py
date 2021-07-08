from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QListView, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from datetime import datetime, timedelta

from PyQt5 import QtGui, QtCore

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from struttura.piscina.corsi.GestioneCorsiPiscina.ControllerGestionePiscina.controller_gestione_corsi_piscina import \
    Controller_GestioneCorsiPiscina


class view_tutti_corsi_piscina(QWidget):

    def __init__(self, data=None, parent=None):
        super(view_tutti_corsi_piscina, self).__init__(parent)
        self.controllore_lista_corsi_piscina = Controller_GestioneCorsiPiscina()
        self.data = data

        self.v_layout = QVBoxLayout()
        self.font = QFont("Yu Gothic UI Light", 13)

        self.label_prenotazioni_by_data = QLabel("Tutte i corsi dalla data di oggi in poi: ")
        self.label_prenotazioni_by_data.setAlignment(Qt.AlignCenter)
        self.label_prenotazioni_by_data.setFont(QFont("Yu Gothic UI Light", 17))
        self.v_layout.addWidget(self.label_prenotazioni_by_data)

        self.lista_corsi_piscina = QListView()
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_corsi_piscina)


        self.h_layout = QHBoxLayout()


        self.bottone_indietro = QPushButton("Chiudi")
        self.bottone_indietro.setFont(self.font)
        self.bottone_indietro.clicked.connect(self.mostra_indietro)
        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro)
        self.bottone_indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_indietro)

        self.v_layout.addLayout(self.h_layout)


        self.setLayout(self.v_layout)

        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        self.setWindowTitle("Elenco Corsi Piscina")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(800, 601))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_corsi = QStandardItemModel()
        for corso in self.controllore_lista_corsi_piscina.get_lista_corsi():
            #per visualizzare solo le date da oggi al futuro
            today=datetime.now()
            yesterday=today - timedelta(1)
            if corso.data>=yesterday:
                item = QStandardItem()
                item.setText("Corso nuoto del " + corso.data.strftime("%d/%m/%Y") + " delle ore " + corso.orario + ", corso: " + corso.corso + " di " + corso.istruttore)
                item.setEditable(False)
                item.setFont(self.font)
                self.modello_lista_corsi.appendRow(item)

        self.lista_corsi_piscina.setModel(self.modello_lista_corsi)


    def mostra_indietro(self):
        self.close()