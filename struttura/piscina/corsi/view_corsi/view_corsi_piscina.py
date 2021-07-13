
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

from struttura.piscina.corsi.corsiPiscina.view_corsi_piscina.view_tutti_corsi_piscina import view_tutti_corsi_piscina
from struttura.piscina.corsi.view_corsi.view_day_corsi_nuoto import view_day_corsi_nuoto


class view_corsi_piscina(QWidget):

    def __init__(self, parent=None):
        super(view_corsi_piscina, self).__init__(parent)

        self.g_layout = QGridLayout()


        self.label_prenotazioni_by_data = QLabel("\nSeleziona una data per visualizzare i dettagli di quel giorno, cliccando Mostra giorno,\nAltrimenti clicca Mostra tutte per visualizzare tutti i corsi di oggi e dei giorni futuri: \n")
        self.label_prenotazioni_by_data.setFont(QFont("Arial", 12))
        self.g_layout.addWidget(self.label_prenotazioni_by_data, 0, 0)

        self.calendario = QCalendarWidget()
        self.calendario.setGridVisible(True)
        self.calendario.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendario.setMinimumDate(QDate(2021, 5, 1))


        data_di_oggi = QTextCharFormat()
        data_di_oggi.setBackground(QColor("sky blue"))
        self.calendario.setDateTextFormat(QDate(datetime.now()),data_di_oggi )
        self.g_layout.addWidget(self.calendario, 1, 0)

        self.h_layout = QHBoxLayout()

        self.crea_pulsante("⬅️", self.mostra_indietro_corsonuoto)
        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro_corsonuoto)


        self.crea_pulsante("Mostra giorno", self.mostra_view_day_nuoto)
        self.shortcut_mostra_giorno = QShortcut(QKeySequence('Return'), self)
        self.shortcut_mostra_giorno.activated.connect(self.mostra_view_day_nuoto)

        self.crea_pulsante("Mostra tutte", self.mostra_tutte_prenotazioni_corsi_nuoto)

        self.g_layout.addLayout(self.h_layout, 2, 0)

        self.setLayout(self.g_layout)

        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco Corsi Piscina")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/sfondonuotosfocato2.jpeg")
        sImage = oImage.scaled(QSize(791, 501))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    #funzione per creare i pulsanti
    def crea_pulsante(self, titolo, funzione):
        pulsante = QPushButton(titolo)
        pulsante.setFont(QFont("Yu Gothic UI Light", 12))
        pulsante.clicked.connect(funzione)
        self.h_layout.addWidget(pulsante)
        pulsante.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    #funzione per creare la pagina
    def mostra_indietro_corsonuoto(self):
        self.close()

    #funzione per mostrare il giorno selezionato
    def mostra_view_day_nuoto(self):
        dataq = self.calendario.selectedDate()
        self.datai = datetime(dataq.year(), dataq.month(), dataq.day())
        self.lista_prenotazioni_day = view_day_corsi_nuoto(self.datai)
        self.lista_prenotazioni_day.show()

    #funzione per mostare tutti i corsi
    def mostra_tutte_prenotazioni_corsi_nuoto(self):
        self.lista_prenotazioni = view_tutti_corsi_piscina()
        self.lista_prenotazioni.show()
