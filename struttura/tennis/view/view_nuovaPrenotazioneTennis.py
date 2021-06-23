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


from ListaPrenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from ListeServizi.model.ListeServizi import ListeServizi
from Prenotazione.model.Prenotazione import Prenotazione

from struttura.tennis.lista_prenotazioniTennis.ControlloreListaTennis.ControlloreListaTennis import \
    ControlloreListaPrenotazioniTennis


class view_nuovaPrenotazioneTennis(QWidget):

    def __init__(self, aggiorna_dati_prenotazioni, parent=None):
        super(view_nuovaPrenotazioneTennis, self).__init__(parent)
        self.font = QFont("Yu Gothic UI Light", 12)
        self.aggiorna_dati_prenotazioni = aggiorna_dati_prenotazioni

        self.layout = QGridLayout()

        # prenotazione data inizio vacanza
        self.label_inizio = QLabel("Seleziona il giorno:")
        self.layout.addWidget(self.label_inizio, 0, 0)

        self.calendario = QCalendarWidget()
        self.calendario.setGridVisible(True)
        self.calendario.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        if datetime.now() > datetime(2021, 6, 1):
            self.calendario.setMinimumDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        else:
            self.calendario.setMinimumDate(QDate(2021, 6, 1))
        self.calendario.setMaximumDate(QDate(2022, 12, 12))

        cell_inizio_start = QTextCharFormat()
        cell_inizio_start.setBackground(QColor("yellow"))
        cell_inizio_stop = QTextCharFormat()
        cell_inizio_stop.setBackground(QColor("red"))
        self.calendario.setDateTextFormat(self.calendario.selectedDate(), cell_inizio_start)
        self.calendario.setDateTextFormat(QDate(2021,9,23), cell_inizio_stop)

        self.layout.addWidget(self.calendario_inizio, 1, 0)

        # prenotazione data fine vacanza
        self.label_fine = QLabel("Seleziona la data:")
        self.layout.addWidget(self.label_fine, 0, 1)

        self.calendario_fine = QCalendarWidget()
        self.calendario_fine.setGridVisible(True)
        self.calendario_fine.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        if datetime.now() > datetime(2021, 6, 1):
            self.calendario_fine.setMinimumDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        else:
            self.calendario_fine.setMinimumDate(QDate(2021, 6, 1))
        self.calendario_fine.setMaximumDate(QDate(2021, 9, 15))

        cell_fine_stop = QTextCharFormat()
        cell_fine_stop.setBackground(QColor("red"))
        self.calendario_fine.setDateTextFormat(QDate(2021, 9, 15), cell_fine_stop)

        self.layout.addWidget(self.calendario_fine, 1, 1)

        # selezione tipologia di alloggio
        self.label_alloggio = QLabel("Seleziona il tipo di alloggio:")
        self.layout.addWidget(self.label_alloggio, 3, 0)

        self.get_servizi()

        # bottone finale di conferma
        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setFont(QFont("Arial", 15, 15, True))
        self.bottone_conferma.clicked.connect(self.aggiungi_prenotazione)
        self.layout.addWidget(self.bottone_conferma, 8, 1)

        self.setLayout(self.layout)
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
    def get_servizi(self):
        self.liste_servizi = ListeServizi()

        self.menu_alloggio = QComboBox()
        self.model_menu_alloggio = QStandardItemModel(self.menu_alloggio)
        for servizio_alloggio in self.liste_servizi.get_servizi_alloggio():
            item = QStandardItem()
            item.setText(servizio_alloggio.nome)
            item.setEditable(False)
            self.model_menu_alloggio.appendRow(item)
        self.menu_alloggio.setModel(self.model_menu_alloggio)
        self.layout.addWidget(self.menu_alloggio, 4, 0)

        self.menu_ristorazione = QComboBox()
        self.model_menu_ristorazione = QStandardItemModel(self.menu_ristorazione)
        for servizio_ristorazione in self.liste_servizi.get_servizi_ristorazione():
            item = QStandardItem()
            item.setText(servizio_ristorazione.nome)
            item.setEditable(False)
            self.model_menu_ristorazione.appendRow(item)
        self.menu_ristorazione.setModel(self.model_menu_ristorazione)
        self.layout.addWidget(self.menu_ristorazione, 7, 0)


    def aggiungi_prenotazione(self):
        data1 = self.calendario_inizio.selectedDate()
        data = datetime(data1.year(), data1.month(), data1.day())

        prenotazione = Prenotazione(data)

        risposta = QMessageBox.question(self, "Conferma", "Il costo della prenotazione è "
                                        + str(prenotazione.get_prezzo_totale()) + "\n\nConfermare?",
                                        QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.No:
            return
        else:
            controllore_lista_prenotazioni = ControlloreListaPrenotazioniTennis()
            controllore_lista_prenotazioni.aggiungi_prenotazione_tennis(prenotazione)
            QMessageBox.about(self, "Confermata", "Prenotazione confermata")
            controllore_lista_prenotazioni.save_data()
            self.aggiorna_dati_prenotazioni()
            self.close()