
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtWidgets import QGridLayout, QCalendarWidget


from PyQt5.QtWidgets import QLabel, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont
from datetime import datetime

from PyQt5 import QtGui, QtCore

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from struttura.tennis.prenotazioniTennis.view_prenotazioniTennis.VistalistaprenotazioniTutte_tennis import \
    VistaListaPrenotazioniTutte
from struttura.tennis.view.view_day_tennis import view_day_tennis


class view_tennis(QWidget):

    def __init__(self, parent=None):
        super(view_tennis, self).__init__(parent)

        self.g_layout = QGridLayout()


        self.label_prenotazioni_by_data = QLabel("\nSeleziona una data per visualizzare i dettagli di quel giorno, cliccando Mostra giorno,\nAltrimenti clicca Mostra tutte per visualizzare tutte le prenotazioni di oggi e future: \n")
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
        self.shortcut_mostra_giorno = QShortcut(QKeySequence('Return'), self)
        self.shortcut_mostra_giorno.activated.connect(self.mostra_view_day_tennis)

        self.crea_pulsante("Mostra tutte", self.mostra_tutte_prenotazioni_tennis)

        self.g_layout.addLayout(self.h_layout, 2, 0)

        self.setLayout(self.g_layout)
        self.setWindowTitle("Lista Prenotazioni")

        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco Prenotazioni Tennis")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/sfondotennissfocato.jpeg")
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


    def mostra_view_day_tennis(self):
        dataq = self.calendario.selectedDate()
        self.datai = datetime(dataq.year(), dataq.month(), dataq.day())
        self.lista_prenotazioni_day = view_day_tennis(self.datai)
        self.lista_prenotazioni_day.show()


    def mostra_tutte_prenotazioni_tennis(self):
        self.lista_prenotazioni = VistaListaPrenotazioniTutte()
        self.lista_prenotazioni.show()
