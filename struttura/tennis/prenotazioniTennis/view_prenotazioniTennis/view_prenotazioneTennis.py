from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QShortcut


#vede i dettagli della singola prenotazione selezionata
class VistaPrenotazioneTennis(QWidget):

    def __init__(self, controllore_prenotazione, parent=None):
        super(VistaPrenotazioneTennis, self).__init__(parent)

        self.controllore_prenotazione = controllore_prenotazione

        self.v_layout = QVBoxLayout()

        #label con i dati della prenotazione
        self.create_label("Giorno:        ", self.controllore_prenotazione.get_giorno_pre_te().strftime('%d/%m/%Y'))
        self.create_label("Orario:        ", self.controllore_prenotazione.get_orario_premuto_pre_te())
        self.create_label("Prenotante:         ", self.controllore_prenotazione.get_nome_pre_te())
        self.create_label("Recapito:            ", self.controllore_prenotazione.get_recapito_pre_te())

        self.h_layout = QHBoxLayout()

        #creazione del pulsante di chiusura
        self.create_button("Chiudi", self.mostra_indietro)

        #shortcut per il tasto di chiusura
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

    #funzione perla creazione dei vari label
    def create_label(self, testo, descrizione):
        h_layout = QHBoxLayout()

        label = QLabel(testo)
        label.setFont(QFont("Yu Gothic UI Light",15))
        h_layout.addWidget(label)


        label_di_testo = QLabel(descrizione)
        label_di_testo.setFont(QFont("Arial",15))
        h_layout.addWidget(label_di_testo)

        self.v_layout.addLayout(h_layout)

    #funzione per la creazione dei vari plsanti
    def create_button(self, titolo, funzione):
        bottone = QPushButton(titolo)
        bottone.setFont(QFont("Yu Gothic UI Light", 12))
        bottone.clicked.connect(funzione)
        self.h_layout.addWidget(bottone)
        bottone.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    #funzione per chiudere la pagina
    def mostra_indietro(self):
        self.close()