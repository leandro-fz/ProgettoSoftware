from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel, QKeySequence
from PyQt5.QtWidgets import QListView, QVBoxLayout, QLabel, QWidget, QPushButton, QMessageBox, QShortcut
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QCalendarWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont
from datetime import datetime
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem, QTextCharFormat, QColor
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QCalendarWidget, QComboBox, QCheckBox, QMessageBox, \
    QPushButton
from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from datetime import datetime, timedelta

from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



from struttura.tennis.lista_prenotazioniTennis.ControlloreListaTennis.ControlloreListaTennis import \
    ControlloreListaPrenotazioniTennis
from struttura.tennis.prenotazioniTennis.controller_prenotazioniTennis.controller_prenotazioniTennis import \
    ControllorePrenotazioneTennis
from struttura.tennis.prenotazioniTennis.model_prenotazioniTennis.model_prenotazioniTennis import \
    model_PrenotazioniTennis
from struttura.tennis.prenotazioniTennis.view_prenotazioniTennis.view_prenotazioneTennis import VistaPrenotazioneTennis


class VistaListaPrenotazioniTutte(QWidget):

    def __init__(self, data=None, parent=None):
        super(VistaListaPrenotazioniTutte, self).__init__(parent)
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioniTennis()
        self.data = data

        self.v_layout = QVBoxLayout()
        self.font = QFont("Yu Gothic UI Light", 13, 13, True)

        if data is not None:
            self.label_prenotazioni_by_data = QLabel("Arrivi del giorno " + data.strftime("%d/%m/%Y") + ":")
        else:
            self.label_prenotazioni_by_data = QLabel("Tutte le prenotazioni: ")
        self.label_prenotazioni_by_data.setAlignment(Qt.AlignCenter)
        self.label_prenotazioni_by_data.setFont(QFont("Yu Gothic UI Light", 17))
        self.v_layout.addWidget(self.label_prenotazioni_by_data)

        self.lista_prenotazioni = QListView()
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_prenotazioni)


        self.h_layout = QHBoxLayout()


        self.bottone_indietro = QPushButton("⬅️")
        self.bottone_indietro.setFont(self.font)
        self.bottone_indietro.clicked.connect(self.mostra_indietro)
        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro)
        self.bottone_indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_indietro)

        self.bottone_elimina = QPushButton("Elimina")
        self.bottone_elimina.setFont(self.font)
        self.bottone_elimina.clicked.connect(self.mostra_elimina)
        self.shortcut_elimina = QShortcut(QKeySequence("Alt+d"), self)
        self.shortcut_elimina.activated.connect(self.mostra_elimina)
        self.bottone_elimina.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_elimina)


        self.bottone_dettagli_prenotazione = QPushButton("Dettagli prenotazione")
        self.bottone_dettagli_prenotazione.setFont(self.font)
        self.bottone_dettagli_prenotazione.clicked.connect(self.dettagli_prenotazione)
        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.dettagli_prenotazione)
        self.h_layout.addWidget(self.bottone_dettagli_prenotazione)
        self.bottone_dettagli_prenotazione.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.v_layout.addLayout(self.h_layout)


        self.setLayout(self.v_layout)
        self.setWindowTitle("Lista Tutte Prenotazioni")

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

    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_prenotazioni = QStandardItemModel()
        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_tennis1():
            #per visualizzare solo le date da oggi al futuro
            today=datetime.now()
            yesterday=today - timedelta(1)
            if prenotazione.data>=yesterday:
                if self.data == prenotazione.data:
                    item = QStandardItem()
                    item.setText("Prenotazione del " + prenotazione.data.strftime("%d/%m/%Y"))
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

    def mostra_indietro(self):
        self.close()

    def mostra_elimina(self):
        pass
    3    # try:
        #     indice = self.lista_prenotazioni.selectedIndexes()[0].row()
        #     da_eliminare = self.controllore_lista_prenotazioni.get_lista_prenotazioni_tennis1()[indice]
        # except:
        #     QMessageBox.critical(self, "Errore", "Seleziona una prenotazione da eliminare", QMessageBox.Ok,QMessageBox.Ok)
        #     return
        #
        # risposta = QMessageBox.question(self, "Elimina prenotazione","Eliminare la prenotazione selezionata?",QMessageBox.Yes,QMessageBox.No)
        # if risposta == QMessageBox.Yes:
        #     self.controllore_lista_prenotazioni.elimina_prenotazione_tennis(da_eliminare)
        #     self.controllore_lista_prenotazioni.save_data()
        #     self.aggiorna_dati_prenotazioni()
        # else:
        #     return

    def dettagli_prenotazione(self):
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            lista_prenotazioni_filtrata = []
            # self.aaco = ControllorePrenotazioneTennis()
            for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_tennis1():
                if prenotazione.data == self.data:
                    # if self.aaco.get_orario_premuto_pre_te() ==
                    lista_prenotazioni_filtrata.append(prenotazione)
            da_visualizzare = lista_prenotazioni_filtrata[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona una prenotazione da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.vista_prenotazione = VistaPrenotazioneTennis(ControllorePrenotazioneTennis(da_visualizzare))
        self.vista_prenotazione.show()