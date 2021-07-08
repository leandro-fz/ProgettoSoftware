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

from struttura.palestra.Corsi.GestioneCorsiPalestra.controller_gestione_corsi_palestra.controller_gestione_corsi_palestra import \
    controller_gestione_corsi_palestra
from struttura.palestra.Corsi.corsiPalestra.controller_corsi_palestra.controller_corsi_palestra import \
    controller_corsi_palestra
from struttura.palestra.Corsi.corsiPalestra.view_corsi_palestra.view_corso_palestra_visualizzazione import \
    view_corso_palestra_visualizzazione
from struttura.palestra.Corsi.view_corsi.view_inserisci_corsi_palestra import view_inserisci_corso_palestra




class view_day_corsi_palestra(QWidget):

    def __init__(self, data, parent=None):
        super(view_day_corsi_palestra, self).__init__(parent)
        self.controller_gestione_palestra = controller_gestione_corsi_palestra()
        self.data = data
        self.v_layout = QVBoxLayout()
        self.font = QFont("Yu Gothic UI Light", 15, 15, False)


        self.label_prenotazioni_by_data = QLabel("Corsi del " + data.strftime("%d/%m/%Y") + ":")
        self.label_prenotazioni_by_data.setAlignment(Qt.AlignCenter)
        self.label_prenotazioni_by_data.setFont(QFont("Yu Gothic UI Light", 12))
        self.v_layout.addWidget(self.label_prenotazioni_by_data)
        self.v_layout.addSpacing(15)

        self.lista_corsi = QListView()
        self.aggiorna_dati_corsi_palestra()
        self.v_layout.addWidget(self.lista_corsi)

        self.h_layout = QHBoxLayout()

        self.bottone_indietro= QPushButton("⬅️")
        self.bottone_indietro.setFont(self.font)
        self.bottone_indietro.clicked.connect(self.mostra_indietro_view_corsi)
        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro_view_corsi)
        self.h_layout.addWidget(self.bottone_indietro)
        self.bottone_indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.bottone_prenotazioni = QPushButton("Dettagli Corso")
        self.bottone_prenotazioni.setFont(self.font)
        self.bottone_prenotazioni.clicked.connect(self.dettagli_prenotazione)
        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.dettagli_prenotazione)
        self.h_layout.addWidget(self.bottone_prenotazioni)
        self.bottone_prenotazioni.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.bottone_aggiungi= QPushButton("Aggiungi Corso")
        self.bottone_aggiungi.setFont(self.font)
        self.bottone_aggiungi.clicked.connect(self.mostra_aggiungi_corso_palestra)
        self.shortcut_aggiungi = QShortcut(QKeySequence('Alt+n'), self)
        self.shortcut_aggiungi.activated.connect(self.mostra_aggiungi_corso_palestra)
        self.h_layout.addWidget(self.bottone_aggiungi)
        self.bottone_aggiungi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.bottone_elimina= QPushButton("Elimina Corso")
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
        self.setWindowTitle("Corsi Palestra")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 501))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    def aggiorna_dati_corsi_palestra(self):
        self.modello_lista_corsi = QStandardItemModel()
        for corso in self.controller_gestione_palestra.get_lista_corsi_palestra():
            if self.data == corso.data:
                item = QStandardItem()
                item.setText("Corso nuoto del " + corso.data.strftime("%d/%m/%Y") + " delle ore " + corso.orario + ", corso: " + corso.corso)
                item.setEditable(False)
                item.setFont(self.font)
                self.modello_lista_corsi.appendRow(item)
        self.lista_corsi.setModel(self.modello_lista_corsi)

    def mostra_indietro_view_corsi(self):
        self.close()

    def mostra_aggiungi_corso_palestra(self):
        today = datetime.now()
        yesterday = today - timedelta(1)
        if self.data <= yesterday:
            QMessageBox.critical(self, "Errore", "Non puoi aggiungere un corso in una data passata", QMessageBox.Ok, QMessageBox.Ok)
            return
        self.vista_nuovo_corso_piscina = view_inserisci_corso_palestra(self.data, self.controller_gestione_palestra, self.aggiorna_dati_corsi_palestra)
        self.vista_nuovo_corso_piscina.show()


    def mostra_elimina(self):
        today = datetime.now()
        yesterday = today - timedelta(1)
        try:
            indice = self.lista_corsi.selectedIndexes()[0].row()
            lista = []
            for corso in self.controller_gestione_palestra.get_lista_corsi_palestra():
                if self.data == corso.data:
                    lista.append(corso)
            da_eliminare = lista[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona una prenotazione da eliminare", QMessageBox.Ok,QMessageBox.Ok)
            return
        if da_eliminare.data < yesterday:
            QMessageBox.critical(self, "Errore", "Non puoi eliminare una prenotazione passata", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Elimina prenotazione","Eliminare la prenotazione?",QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.controller_gestione_palestra.elimina_corso_palestra(da_eliminare.id)
            QMessageBox.about(self, "Eliminato", "La prenotazione è stato eliminata")
            self.aggiorna_dati_corsi_palestra()
        else:
            return

    def dettagli_prenotazione(self):
        try:
            indice = self.lista_corsi.selectedIndexes()[0].row()
            lista = []
            for corso in self.controller_gestione_palestra.get_lista_corsi_palestra():
                if self.data == corso.data:
                    lista.append(corso)
            da_visualizzare = lista[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona un corso da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.vista_prenotazione = view_corso_palestra_visualizzazione(controller_corsi_palestra(da_visualizzare))
        self.vista_prenotazione.show()

    def closeEvent(self, event):
        self.controller_gestione_palestra.save_data()