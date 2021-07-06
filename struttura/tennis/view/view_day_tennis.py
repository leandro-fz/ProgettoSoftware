from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtCore import Qt


from PyQt5.QtWidgets import QVBoxLayout, QLabel, QListView, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem

from PyQt5 import QtGui, QtCore

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime, timedelta

from struttura.tennis.lista_prenotazioniTennis.ControlloreListaTennis.ControlloreListaTennis import \
    ControlloreListaPrenotazioniTennis
from struttura.tennis.prenotazioniTennis.controller_prenotazioniTennis.controller_prenotazioniTennis import \
    ControllorePrenotazioneTennis
from struttura.tennis.prenotazioniTennis.view_prenotazioniTennis.view_prenotazioneTennis import VistaPrenotazioneTennis
from struttura.tennis.view.view_nuovaPrenotazioneTennis import view_nuovaPrenotazioneTennis


class view_day_tennis(QWidget):

    def __init__(self, data, parent=None):
        super(view_day_tennis, self).__init__(parent)
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioniTennis()
        self.data = data
        self.v_layout = QVBoxLayout()
        self.font = QFont("Yu Gothic UI Light", 15, 15, False)


        self.label_prenotazioni_by_data = QLabel("Prenotazioni del giorno " + data.strftime("%d/%m/%Y") + ":")
        self.label_prenotazioni_by_data.setAlignment(Qt.AlignCenter)
        self.label_prenotazioni_by_data.setFont(QFont("Yu Gothic UI Light", 12))
        self.v_layout.addWidget(self.label_prenotazioni_by_data)
        self.v_layout.addSpacing(15)

        self.lista_prenotazioni = QListView()
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_prenotazioni)

        self.h_layout = QHBoxLayout()

        self.bottone_indietro= QPushButton("⬅️")
        self.bottone_indietro.setFont(self.font)
        self.bottone_indietro.clicked.connect(self.mostra_indietro_view_tennis)
        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro_view_tennis)
        self.h_layout.addWidget(self.bottone_indietro)
        self.bottone_indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.bottone_prenotazioni = QPushButton("Dettagli prenotazione")
        self.bottone_prenotazioni.setFont(self.font)
        self.bottone_prenotazioni.clicked.connect(self.dettagli_prenotazione)
        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.dettagli_prenotazione)
        self.h_layout.addWidget(self.bottone_prenotazioni)
        self.bottone_prenotazioni.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.bottone_aggiungi= QPushButton("Aggiungi")
        self.bottone_aggiungi.setFont(self.font)
        self.bottone_aggiungi.clicked.connect(self.mostra_aggiungi)
        self.shortcut_aggiungi = QShortcut(QKeySequence('Alt+n'), self)
        self.shortcut_aggiungi.activated.connect(self.mostra_aggiungi)
        self.h_layout.addWidget(self.bottone_aggiungi)
        self.bottone_aggiungi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.bottone_elimina= QPushButton("Elimina")
        self.bottone_elimina.setFont(self.font)
        self.bottone_elimina.clicked.connect(self.mostra_elimina)
        self.shortcut_elimina = QShortcut(QKeySequence('Alt+d'), self)
        self.shortcut_elimina.activated.connect(self.mostra_elimina)
        self.h_layout.addWidget(self.bottone_elimina)
        self.bottone_elimina.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.v_layout.addLayout(self.h_layout)


        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Prenotazioni Tennis")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 501))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_prenotazioni = QStandardItemModel()
        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_tennis1():
            if self.data == prenotazione.data:
                item = QStandardItem()
                item.setText("Prenotazione del " + prenotazione.data.strftime("%d/%m/%Y") + " delle ore " + prenotazione.orario + " di " + prenotazione.utente)
                item.setEditable(False)
                item.setFont(self.font)
                self.modello_lista_prenotazioni.appendRow(item)
        self.lista_prenotazioni.setModel(self.modello_lista_prenotazioni)

    def mostra_indietro_view_tennis(self):
        self.close()

    def mostra_aggiungi(self):
        today = datetime.now()
        yesterday = today - timedelta(1)
        if self.data <= yesterday:
            risposta = QMessageBox.question(self, "Conferma", "Vuoi aggiungere una prenotazione passata?" + "\n\nConfermare?", QMessageBox.Yes, QMessageBox.No)
            if risposta == QMessageBox.No:
                return
        self.vista_nuova_prenotazione = view_nuovaPrenotazioneTennis(self.data, self.controllore_lista_prenotazioni, self.aggiorna_dati_prenotazioni)
        self.vista_nuova_prenotazione.show()

    # def closeEvent(self, event):
    #     self.controllore_lista_prenotazioni.save_data()

    def mostra_elimina(self):
        today = datetime.now()
        yesterday = today - timedelta(1)
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            lista = []
            for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_tennis1():
                if self.data == prenotazione.data:
                    lista.append(prenotazione)
            da_eliminare = lista[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona una prenotazione da eliminare", QMessageBox.Ok,QMessageBox.Ok)
            return
        if da_eliminare.data < yesterday:
            QMessageBox.critical(self, "Errore", "Non puoi eliminare una prenotazione passata", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Elimina prenotazione","Eliminare la prenotazione?",QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.controllore_lista_prenotazioni.elimina_prenotazione_tennis(da_eliminare.id)
            QMessageBox.about(self, "Eliminato", "La prenotazione è stato eliminata")
            # self.controllore_lista_prenotazioni.save_data()
            self.aggiorna_dati_prenotazioni()
        else:
            return

    def dettagli_prenotazione(self):
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            lista = []
            for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_tennis1():
                if self.data == prenotazione.data:
                    lista.append(prenotazione)
            da_visualizzare = lista[indice]
            # da_visualizzare = self.controllore_lista_prenotazioni.get_lista_prenotazioni_tennis_by_day(self.data)[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona una prenotazione da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.vista_prenotazione = VistaPrenotazioneTennis(ControllorePrenotazioneTennis(da_visualizzare))
        self.vista_prenotazione.show()

    def closeEvent(self, event):
        self.controllore_lista_prenotazioni.save_data()