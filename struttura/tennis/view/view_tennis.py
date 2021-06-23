from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from datetime import datetime

from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



from struttura.tennis.lista_prenotazioniTennis.ControlloreListaTennis.ControlloreListaTennis import \
    ControlloreListaPrenotazioniTennis
from struttura.tennis.view.view_nuovaPrenotazioneTennis import view_nuovaPrenotazioneTennis


class view_tennis(QWidget):

    def __init__(self, parent=None):
        super(view_tennis, self).__init__(parent)
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioniTennis()

        self.v_layout = QVBoxLayout()

        self.label_prenotazioni = QLabel("Prenotazioni Tennis: ")
        self.label_prenotazioni.setFont(QFont("Yu Gothic UI Light", 12))
        self.v_layout.addWidget(self.label_prenotazioni)

        self.lista_prenotazioni = QListView()
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_prenotazioni)

        self.h_layout = QHBoxLayout()

        self.crea_pulsante("⬅️", self.mostra_indietro_tennis)
        self.crea_pulsante("Nuova prenotazione", self.mostra_nuova_prenotazione_tennis)
        self.crea_pulsante("Apri prenotazione", self.mostra_apri_prenotazione_tennis)
        self.crea_pulsante("Elimina prenotazione", self.mostra_elimina_prenotazione_tennis)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco Prenotazioni Tennis")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 501))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    def crea_pulsante(self, titolo, funzione):
        pulsante = QPushButton(titolo)
        pulsante.setFont(QFont("Yu Gothic UI Light", 12))
        pulsante.clicked.connect(funzione)
        self.h_layout.addWidget(pulsante)

    def mostra_indietro_tennis(self):
        self.close()

    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_prenotazioni = QStandardItemModel()
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioniTennis()
        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente():
            item = QStandardItem()
            item.setText("Prenotazione del " + prenotazione.data_inizio.strftime("%d/%m/%Y"))
            item.setEditable(False)
            item.setFont(QFont("Yu Gothic UI Light", 12))
            self.modello_lista_prenotazioni.appendRow(item)
        self.lista_prenotazioni.setModel(self.modello_lista_prenotazioni)

    def mostra_nuova_prenotazione_tennis(self):
        self.vista_nuova_prenotazione = view_nuovaPrenotazioneTennis(self.aggiorna_dati_prenotazioni)
        self.vista_nuova_prenotazione.show()

    def mostra_apri_prenotazione_tennis(self):
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            da_visualizzare = self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona la prenotazione da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.vista_prenotazione = VistaPrenotazione(ControllorePrenotazione(da_visualizzare))
        self.vista_prenotazione.show()

    def mostra_elimina_prenotazione_tennis(self):
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            da_eliminare = self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona la prenotazione da eliminare", QMessageBox.Ok,QMessageBox.Ok)
            return

        if da_eliminare.data_inizio < datetime.now():
            QMessageBox.critical(self, "Errore", "Non puoi eliminare prenotazioni passate", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Elimina prenotazione",
                               "Sei sicuro di voler elimare la prenotazione selezionata? \nPerderai la caparra versata", QMessageBox.Yes,
                               QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.controllore_lista_prenotazioni.elimina_prenotazione_singola( da_eliminare.data_inizio)
            self.controllore_lista_prenotazioni.save_data()
            self.aggiorna_dati_prenotazioni()
        else:
            return