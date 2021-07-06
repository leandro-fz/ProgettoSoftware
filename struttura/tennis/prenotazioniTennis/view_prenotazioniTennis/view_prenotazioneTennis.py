from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QShortcut


from struttura.tennis.lista_prenotazioniTennis.ControlloreListaTennis.ControlloreListaTennis import \
    ControlloreListaPrenotazioniTennis


class VistaPrenotazioneTennis(QWidget):

    def __init__(self, controllore_prenotazione, parent=None):
        super(VistaPrenotazioneTennis, self).__init__(parent)

        self.controllore_prenotazione = controllore_prenotazione

        self.v_layout = QVBoxLayout()

        # labels contenenti dati del cliente
        self.create_label("Giorno:        ", self.controllore_prenotazione.get_giorno_pre_te().strftime('%d/%m/%Y'))
        self.create_label("Orario:        ", self.controllore_prenotazione.get_orario_premuto_pre_te())
        self.create_label("Prenotatore:         ", self.controllore_prenotazione.get_nome_pre_te())
        self.create_label("Recapito:            ", self.controllore_prenotazione.get_recapito_pre_te())

        self.h_layout = QHBoxLayout()

        # bottoni profilo cliente collegati alle relative funzioni
        self.create_button("Chiudi", self.mostra_indietro)
        # self.create_button("Elimina", self.conferma_eliminazione)

        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro)

        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

        self.setMinimumSize(500, 300)
        self.setMaximumSize(500, 300)
        self.setWindowTitle("Prenotazione Tennis")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
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

    # def conferma_eliminazione(self):
    #
    #     self.controllore_lista_prenotazioi_tennis = ControlloreListaPrenotazioniTennis()
    #     risposta = QMessageBox.warning(self, "Elimina Prenotazione", "Sei sicuro di voler elimare la prenotazione?", QMessageBox.Yes, QMessageBox.No)
    #     if risposta == QMessageBox.Yes:
    #         self.close()
    #         self.controllore_lista_prenotazioi_tennis.elimina_prenotazione_tennis(self.controllore_prenotazione.get_id_pre_te())
    #         self.controllore_lista_prenotazioi_tennis.save_data()
    #     else:
    #         return