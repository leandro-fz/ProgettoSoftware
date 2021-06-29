from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel, QKeySequence
from PyQt5.QtWidgets import QListView, QVBoxLayout, QLabel, QWidget, QPushButton, QMessageBox, QShortcut
from PyQt5.QtCore import Qt



from struttura.tennis.lista_prenotazioniTennis.ControlloreListaTennis.ControlloreListaTennis import \
    ControlloreListaPrenotazioniTennis
from struttura.tennis.prenotazioniTennis.controller_prenotazioniTennis.controller_prenotazioniTennis import \
    ControllorePrenotazioneTennis
from struttura.tennis.prenotazioniTennis.view_prenotazioniTennis.view_prenotazioneTennis import VistaPrenotazioneTennis


class VistaListaPrenotazioniTutte(QWidget):

    def __init__(self, data=None, parent=None):
        super(VistaListaPrenotazioniTutte, self).__init__(parent)
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioniTennis()
        self.data = data

        self.v_layout = QVBoxLayout()
        self.font = QFont("Yu Gothic UI Light", 15, 15, True)

        if data is not None:
            self.label_prenotazioni_by_data = QLabel("Arrivi del giorno " + data.strftime("%d/%m/%Y") + ":")
        else:
            self.label_prenotazioni_by_data = QLabel("Tutte le prenotazioni: ")
        self.label_prenotazioni_by_data.setAlignment(Qt.AlignCenter)
        self.v_layout.addWidget(self.label_prenotazioni_by_data)
        self.v_layout.addSpacing(30)

        self.lista_prenotazioni = QListView()
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_prenotazioni)

        self.bottone_dettagli_prenotaizone = QPushButton("Dettagli prenotazione")
        self.bottone_dettagli_prenotaizone.setFont(self.font)
        self.bottone_dettagli_prenotaizone.clicked.connect(self.dettagli_prenotazione)
        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.dettagli_prenotazione)
        self.v_layout.addWidget(self.bottone_dettagli_prenotaizone)

        self.setLayout(self.v_layout)
        self.resize(900, 600)
        self.setWindowTitle("Lista Prenotazioni")

    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_prenotazioni = QStandardItemModel()

        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_tennis():

            if self.data == prenotazione.data:
                item = QStandardItem()
                item.setText("Prenotazione del " + prenotazione.data.strftime("%d/%m/%Y"))
                             # + " effettuata da " + prenotazione.email_cliente)
                item.setEditable(False)
                item.setFont(self.font)
                self.modello_lista_prenotazioni.appendRow(item)
            elif self.data is None:
                item = QStandardItem()
                item.setText("Prenotazione del " + prenotazione.data.strftime("%d/%m/%Y"))
                item.setEditable(False)
                item.setFont(self.font)
                self.modello_lista_prenotazioni.appendRow(item)

        self.lista_prenotazioni.setModel(self.modello_lista_prenotazioni)

    def dettagli_prenotazione(self):
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            lista_prenotazioni_filtrata = []
            for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_tennis():
                if prenotazione.data == self.data:
                    lista_prenotazioni_filtrata.append(prenotazione)
            da_visualizzare = lista_prenotazioni_filtrata[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona la prenotazione da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.vista_prenotazione = VistaPrenotazioneTennis(ControllorePrenotazioneTennis(da_visualizzare))
        self.vista_prenotazione.show()