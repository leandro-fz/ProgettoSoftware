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



from struttura.tennis.lista_prenotazioniTennis.ControlloreListaTennis.ControlloreListaTennis import \
    ControlloreListaPrenotazioniTennis
from struttura.tennis.prenotazioniTennis.model_prenotazioniTennis.model_prenotazioniTennis import \
    model_PrenotazioniTennis


class view_nuovaPrenotazioneTennis(QWidget):

    def __init__(self, aggiorna_dati_prenotazioni, parent=None):
        super(view_nuovaPrenotazioneTennis, self).__init__(parent)
        self.font = QFont("Yu Gothic UI Light", 15)
        self.aggiorna_dati_prenotazioni = aggiorna_dati_prenotazioni

        self.layout = QGridLayout()

        # prenotazione data inizio vacanza
        self.label_inizio = QLabel("Seleziona il giorno:")
        self.layout.addWidget(self.label_inizio, 0, 0)

        self.calendario = QCalendarWidget()
        self.calendario.setGridVisible(True)
        self.calendario.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        # if datetime.now() > datetime(2021, 6, 1):
        #     self.calendario.setMinimumDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        # else:
        self.calendario.setMinimumDate(QDate(2021, 5, 1))
        # self.calendario.setMaximumDate(QDate(2022, 12, 30))
        #
        # cell_inizio_start = QTextCharFormat()
        # cell_inizio_start.setBackground(QColor("white"))
        # cell_inizio_stop = QTextCharFormat()
        # cell_inizio_stop.setBackground(QColor("red"))
        # self.calendario.setDateTextFormat(self.calendario.selectedDate(), cell_inizio_start)
        # self.calendario.setDateTextFormat(QDate(2021,9,23), cell_inizio_stop)

        self.layout.addWidget(self.calendario)

        #
        # self.calendario_fine = QCalendarWidget()
        # self.calendario_fine.setGridVisible(True)
        # self.calendario_fine.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        # if datetime.now() > datetime(2021, 6, 1):
        #     self.calendario_fine.setMinimumDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        # else:
        #     self.calendario_fine.setMinimumDate(QDate(2021, 6, 1))
        # self.calendario_fine.setMaximumDate(QDate(2021, 9, 15))
        #
        # cell_fine_stop = QTextCharFormat()
        # cell_fine_stop.setBackground(QColor("red"))
        # self.calendario_fine.setDateTextFormat(QDate(2021, 9, 15), cell_fine_stop)

        # self.layout.addWidget(self.calendario_fine, 1, 1)

        # selezione tipologia di alloggio
        # self.label_alloggio = QLabel("Seleziona il tipo di alloggio:")
        # self.layout.addWidget(self.label_alloggio, 3, 0)

        # self.h_layout = QHBoxLayout()

        self.bottone_indietro = QPushButton("⬅️")
        self.bottone_indietro.setFont(QFont("Yu Gothic UI Light", 15, 15, True))
        self.bottone_indietro.clicked.connect(self.indietro_prenotazione)
        self.layout.addWidget(self.bottone_indietro)
        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.indietro_prenotazione)
        self.bottone_indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setFont(QFont("Yu Gothic UI Light", 15, 15, True))
        self.bottone_conferma.clicked.connect(self.aggiungi_prenotazione)
        self.layout.addWidget(self.bottone_conferma)
        self.shortcut_conferma = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_conferma.activated.connect(self.aggiungi_prenotazione)
        self.bottone_conferma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # self.layout.addLayout(self.h_layout)

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

    def indietro_prenotazione(self):
        self.close()

    def aggiungi_prenotazione(self):
        data1 = self.calendario.selectedDate()
        data = datetime(data1.year(), data1.month(), data1.day())

        prenotazione = model_PrenotazioniTennis(data)

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