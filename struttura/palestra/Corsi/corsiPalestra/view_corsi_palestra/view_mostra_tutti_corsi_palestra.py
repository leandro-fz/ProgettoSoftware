from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QListView, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from datetime import datetime, timedelta

from PyQt5 import QtGui, QtCore

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from struttura.palestra.Corsi.GestioneCorsiPalestra.controller_gestione_corsi_palestra.controller_gestione_corsi_palestra import \
    controller_gestione_corsi_palestra

#visualizza tutti i corsi di palstra

class view_mostra_tutti_corsi_palestra(QWidget):

    def __init__(self, data=None, parent=None):
        super(view_mostra_tutti_corsi_palestra, self).__init__(parent)
        self.controller_gestione_corsi_palestra = controller_gestione_corsi_palestra()
        self.data = data

        self.v_layout = QVBoxLayout()
        self.font = QFont("Yu Gothic UI Light", 13)

        self.label_prenotazioni_by_data = QLabel("Tutte i corsi dalla data di oggi in poi: ")
        self.label_prenotazioni_by_data.setAlignment(Qt.AlignCenter)
        self.label_prenotazioni_by_data.setFont(QFont("Yu Gothic UI Light", 17))
        self.v_layout.addWidget(self.label_prenotazioni_by_data)

        self.lista_corsi_palestra = QListView()
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_corsi_palestra)


        self.h_layout = QHBoxLayout()

        #pulsante chiudi
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
        self.setWindowTitle("Elenco Corsi Palestra")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(800, 601))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    #funzione che serve a visualizzare tutti i corsi della palestra
    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_corsi = QStandardItemModel()
        for corso in self.controller_gestione_corsi_palestra.get_lista_corsi_palestra():
            #per visualizzare solo le date da oggi al futuro
            today=datetime.now()
            yesterday=today - timedelta(1)
            if corso.data>=yesterday:
                item = QStandardItem()
                item.setText("Corso palestra del " + corso.data.strftime("%d/%m/%Y") + " delle ore " + corso.orario + ", corso: " + corso.corso + " di " + corso.istruttore)
                item.setEditable(False)
                item.setFont(self.font)
                self.modello_lista_corsi.appendRow(item)

        self.lista_corsi_palestra.setModel(self.modello_lista_corsi)

    #funzione di chiusura della pagina
    def mostra_indietro(self):
        self.close()