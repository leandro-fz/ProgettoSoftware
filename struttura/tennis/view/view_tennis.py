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
from datetime import datetime

from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from struttura.tennis.prenotazioniTennis.view_prenotazioniTennis.VistalistaprenotazioniTutte_tennis import \
    VistaListaPrenotazioniTutte
from struttura.tennis.view.view_day_tennis import view_day_tennis
from struttura.tennis.view.view_nuovaPrenotazioneTennis import view_nuovaPrenotazioneTennis


class view_tennis(QWidget):

    def __init__(self, parent=None):
        super(view_tennis, self).__init__(parent)

        self.g_layout = QGridLayout()


        self.label_prenotazioni_by_data = QLabel("\nSeleziona una data, poi clicca i pulsanti desiderati: \n")
        self.label_prenotazioni_by_data.setFont(QFont("Yu Gothic UI Light", 12))
        self.g_layout.addWidget(self.label_prenotazioni_by_data, 0, 0)

        self.calendario = QCalendarWidget()
        self.calendario.setGridVisible(True)
        self.calendario.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendario.setMinimumDate(QDate(2021, 5, 1))


        data_di_oggi = QTextCharFormat()
        data_di_oggi.setBackground(QColor("yellow"))
        self.calendario.setDateTextFormat(QDate(datetime.now()),data_di_oggi )
        self.g_layout.addWidget(self.calendario, 1, 0)

        self.h_layout = QHBoxLayout()

        self.crea_pulsante("⬅️", self.mostra_indietro_tennis)
        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro_tennis)


        self.crea_pulsante("Mostra giorno", self.mostra_view_day_tennis)

        self.crea_pulsante("Mostra tutte", self.mostra_tutte_prenotazioni_tennis)

        self.g_layout.addLayout(self.h_layout, 2, 0)

        self.setLayout(self.g_layout)
        self.setWindowTitle("Lista Prenotazioni")

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
        pulsante.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def mostra_indietro_tennis(self):
        self.close()

    # def mostra_vedi(self):
    #     pass
        # data_selezionata = self.calendario.selectedDate()
        # self.data_selezionata = datetime(data_selezionata.year(), data_selezionata.month(), data_selezionata.day())
        # self.lista_prenotazioni_by_data_Selezionata = VistaListaPrenotazioniAdmin(self.data_inizio)
        # self.lista_prenotazioni_by_data_Selezionata.show()

    def mostra_view_day_tennis(self):
        dataq = self.calendario.selectedDate()
        self.datai = datetime(dataq.year(), dataq.month(), dataq.day())
        self.lista_prenotazioni_day = view_day_tennis(self.datai)
        self.lista_prenotazioni_day.show()
    # def mostra_apri_prenotazione_tennis(self):
    #     try:
    #         indice = self.lista_prenotazioni.selectedIndexes()[0].row()
    #         da_visualizzare = self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente()[indice]
    #     except:
    #         QMessageBox.critical(self, "Errore", "Seleziona una prenotazione", QMessageBox.Ok, QMessageBox.Ok)
    #         return
    #
    #     self.vista_prenotazione = view_nuovaPrenotazioneTennis(ControllorePrenotazioneTennis(da_visualizzare))
    #     self.vista_prenotazione.show()

    # def mostra_elimina_prenotazione_tennis(self):
    #     try:
    #         indice = self.lista_prenotazioni.selectedIndexes()[0].row()
    #         da_eliminare = self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente()[indice]
    #     except:
    #         QMessageBox.critical(self, "Errore", "Seleziona la prenotazione da eliminare", QMessageBox.Ok,QMessageBox.Ok)
    #         return
    #
    #     risposta = QMessageBox.question(self, "Elimina prenotazione",
    #                            "Elimare la prenotazione selezionata?", QMessageBox.Yes, QMessageBox.No)
    #     if risposta == QMessageBox.Yes:
    #         self.controllore_lista_prenotazioni.elimina_prenotazione_singola( da_eliminare.data_inizio)
    #         self.controllore_lista_prenotazioni.save_data()
    #         self.aggiorna_dati_prenotazioni()
    #     else:
    #         return

    def mostra_tutte_prenotazioni_tennis(self):
        return
        # self.lista_prenotazioni = VistaListaPrenotazioniTutte()
        # self.lista_prenotazioni.show()
