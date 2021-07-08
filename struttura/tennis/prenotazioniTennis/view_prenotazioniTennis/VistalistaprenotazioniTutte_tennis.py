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



from struttura.tennis.lista_prenotazioniTennis.ControlloreListaTennis.ControlloreListaTennis import \
    ControlloreListaPrenotazioniTennis


class VistaListaPrenotazioniTutte(QWidget):

    def __init__(self, data=None, parent=None):
        super(VistaListaPrenotazioniTutte, self).__init__(parent)
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioniTennis()
        self.data = data

        self.v_layout = QVBoxLayout()
        self.font = QFont("Yu Gothic UI Light", 13)

        self.label_prenotazioni_by_data = QLabel("Tutte le prenotazioni dalla data di oggi in poi: ")
        self.label_prenotazioni_by_data.setAlignment(Qt.AlignCenter)
        self.label_prenotazioni_by_data.setFont(QFont("Yu Gothic UI Light", 17))
        self.v_layout.addWidget(self.label_prenotazioni_by_data)

        self.lista_prenotazioni = QListView()
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_prenotazioni)


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
        self.setWindowTitle("Elenco Prenotazioni Tennis")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/sfondotennissfocato.jpeg")
        sImage = oImage.scaled(QSize(800, 601))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_prenotazioni = QStandardItemModel()
        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_tennis1():
            #per visualizzare solo le date da oggi al futuro
            today=datetime.now()
            yesterday=today - timedelta(1)
            if prenotazione.data>=yesterday:
                item = QStandardItem()
                item.setText("Prenotazione del " + prenotazione.data.strftime("%d/%m/%Y") + " delle ore " + prenotazione.orario + " di " + prenotazione.utente + ", recapito: " + prenotazione.recapito)
                item.setEditable(False)
                item.setFont(self.font)
                self.modello_lista_prenotazioni.appendRow(item)

        self.lista_prenotazioni.setModel(self.modello_lista_prenotazioni)


    def mostra_indietro(self):
        self.close()