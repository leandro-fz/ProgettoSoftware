from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from struttura.tennis.prenotazioniTennis.controller_prenotazioniTennis.controller_prenotazioniTennis import \
    ControllorePrenotazioneTennis


class VistaPrenotazioneTennis(QWidget):
    def __init__(self, controllore_prenotazione, parent=None):
        super(VistaPrenotazioneTennis, self).__init__(parent)
        self.controllore_prenotazione = controllore_prenotazione
        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Yu Gothic UI Light", 14)
        self.font_label.setBold(True)

        self.font_campi = QFont("Yu Gothic UI Light", 14)

        self.label_nome = QLabel("Prenotatore:")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.campo_nome.setFont(self.font_campi)
        self.campo_nome.setText(self.controllore_prenotazione.get_nome_pre_te())
        self.v_layout.addWidget(self.campo_nome)

        # self.label_orario = QLabel("Orario:")
        # self.label_orario.setFont(self.font_label)
        # self.v_layout.addWidget(self.label_orario)
        #
        # self.campo_orario = QLineEdit()
        # self.campo_orario.setFont(self.font_campi)
        # self.campo_orario.setText(self.controllore_prenotazione.get_orario_premuto_pre_te())
        # self.v_layout.addWidget(self.campo_orario)

        # self.label_giorno = QLabel("Giorno:")
        # self.label_giorno.setFont(self.font_label)
        # self.v_layout.addWidget(self.label_giorno)

        # self.campo_giorno = QLineEdit()
        # self.campo_giorno.setFont(self.font_campi)
        # self.stringa = str(self.controllore_prenotazione.get_giorno_pre_te().strftime("%d/%m/%Y"))
        # self.campo_giorno.setText(self.stringa)
        # self.v_layout.addWidget(self.campo_giorno)

        self.label_recapito = QLabel("Recapito")
        self.label_recapito.setFont(self.font_label)
        self.v_layout.addWidget(self.label_recapito)

        self.campo_recapito = QLineEdit()
        self.campo_recapito.setFont(self.font_campi)
        self.campo_recapito.setText(self.controllore_prenotazione.get_recapito_pre_te())
        # self.stringa2 = str(self.controllore_prenotazione.get_orario_premuto_pre_te())
        # self.campo_recapito.setText(self.stringa2)
        self.v_layout.addWidget(self.campo_recapito)


        self.h_layout = QHBoxLayout()

        self.bottone_chiudi = QPushButton("Chiudi")
        self.bottone_chiudi.setFont(self.font_campi)
        self.bottone_chiudi.clicked.connect(self.chiudi_finestra)
        self.bottone_chiudi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_chiudi)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Prenotazione")
        self.resize(300, 400)

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 610)
        self.setMaximumSize(781, 610)
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 611))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    def chiudi_finestra(self):
        self.close()