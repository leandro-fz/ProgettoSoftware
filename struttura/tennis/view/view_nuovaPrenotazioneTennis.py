from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem, QTextCharFormat, QColor
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QCalendarWidget, QComboBox, QCheckBox, QMessageBox, \
    QPushButton
from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QHBoxLayout, QPushButton, QMessageBox, QComboBox
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

    def __init__(self, data, aggiorna_dati_prenotazioni, parent=None):
        super(view_nuovaPrenotazioneTennis, self).__init__(parent)
        self.font = QFont("Yu Gothic UI Light", 15)
        self.aggiorna_dati_prenotazioni = aggiorna_dati_prenotazioni
        self.data1 = data


        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Yu Gothic UI Light", 15)
        self.font_label.setBold(True)

        self.font_label2 = QFont("Yu Gothic UI Light", 15)
        self.label_alto = QLabel("Compila il form di prenotazione tennis")
        self.label_alto.setFont(self.font_label2)
        self.v_layout.addWidget(self.label_alto)

        # self.v_layout.addSpacing(10)

        self.label_prenotatore = QLabel("Prenotatore")
        self.label_prenotatore.setFont(self.font_label)
        self.v_layout.addWidget(self.label_prenotatore)

        self.campo_prenotatore = QLineEdit()
        self.v_layout.addWidget(self.campo_prenotatore)

        self.label_recapito = QLabel("Recapito telefonico")
        self.label_recapito.setFont(self.font_label)
        self.v_layout.addWidget(self.label_recapito)

        self.campo_recapito = QLineEdit()
        self.v_layout.addWidget(self.campo_recapito)

        # self.label_numeroutenti = QLabel("Numero Giocatori")
        # self.label_numeroutenti.setFont(self.font_label)
        # self.v_layout.addWidget(self.label_numeroutenti)
        #
        # self.campo_numeroutenti = QLineEdit()
        # self.v_layout.addWidget(self.campo_numeroutenti)

        #orario
        self.label_data = QLabel("Orario")
        self.label_data.setFont(self.font_label)
        self.v_layout.addWidget(self.label_data)

        # self.campo_data = QLineEdit()
        # self.v_layout.addWidget(self.campo_data)

        self.combo = QComboBox(self)
        self.combo.addItem("Seleziona un orario")
        self.combo.addItem("08:00-09:00")
        self.combo.addItem("09:00-10:00")
        self.combo.addItem("10:00-11:00")
        self.combo.addItem("11:00-12:00")
        self.combo.addItem("12:00-13:00")
        self.combo.addItem("13:00-14:00")
        self.combo.addItem("14:00-15:00")
        self.combo.addItem("15:00-16:00")
        self.combo.addItem("16:00-17:00")
        self.combo.addItem("17:00-18:00")
        self.combo.addItem("18:00-19:00")
        self.combo.addItem("19:00-20:00")
        self.combo.addItem("20:00-21:00")
        self.combo.addItem("21:00-22:00")
        self.combo.addItem("22:00-23:00")

        self.v_layout.addWidget(self.combo)



        # self.combo = QComboBox("Orario")
        # self.combo.setFont(self.font_label)
        # self.combo.setItemText(0, "0")
        # self.combo.setItemText(1, "2")
        # self.v_layout.addWidget(self.combo)
        #
        # self.campo_combo = QLineEdit()
        # self.v_layout.addWidget(self.campo_combo)

        self.v_layout.addSpacing(10)
        self.font_label.setBold(False)

        self.h_layout = QHBoxLayout()

        self.bottone_annulla = QPushButton("Annulla")
        self.bottone_annulla.setFont(self.font_label)
        self.bottone_annulla.clicked.connect(self.mostra_annulla_ins)
        self.h_layout.addWidget(self.bottone_annulla)
        self.bottone_annulla.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.bottone_conferma = QPushButton("Conferma")
        self.h_layout.addWidget(self.bottone_conferma)
        self.bottone_conferma.clicked.connect(self.conferma_inserimento)
        self.bottone_conferma.setFont(self.font_label)
        self.bottone_conferma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shortcut_conferma = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_conferma.activated.connect(self.conferma_inserimento)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuova Prenotazione Tennis")
        self.resize(300, 400)

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 501))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


    def mostra_annulla_ins(self):
        reply = QMessageBox.question(self, 'Annullare', 'Sei sicuro di voler uscire?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            return


    def indietro_prenotazione(self):
        self.close()

    def conferma_inserimento(self):
        utente = self.campo_prenotatore.text()
        recapito = self.campo_recapito.text()
        # numero = self.campo_numeroutenti.text()
        orario_premuto = str(self.combo.currentText())
        dataselezionata = self.data1
        # datetime(self.data1.year(), self.data1.month(), self.data1.day())

        if utente == "" or recapito == "":
            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        # try:
        #     numero = int(self.campo_numeroutenti.text())
        # except:
        #     QMessageBox.critical(self, "Errore", "Il numero degli utenti non può avere lettere", QMessageBox.Ok, QMessageBox.Ok)
        #     return

        if orario_premuto == "Seleziona un orario":
            QMessageBox.critical(self, "Errore", "Seleziona un orario valido ", QMessageBox.Ok, QMessageBox.Ok)
            return

        if not self.controlla_disponibilità(dataselezionata, orario_premuto):
            QMessageBox.critical(self, "Conflitto", "Campo già prenotato",QMessageBox.Ok, QMessageBox.Ok)
            return

        prenotazione = model_PrenotazioniTennis(utente, dataselezionata, orario_premuto, recapito)


        risposta = QMessageBox.question(self, "Conferma", "Il costo della prenotazione è "+ str(prenotazione.get_prezzo_totale()) + "\n\nConfermare?",QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.No:
            return
        else:
            controllore_lista_prenotazioni = ControlloreListaPrenotazioniTennis()
            controllore_lista_prenotazioni.aggiungi_prenotazione_tennis(prenotazione)
            QMessageBox.about(self, "Confermata", "Prenotazione confermata")
            controllore_lista_prenotazioni.save_data()
            self.aggiorna_dati_prenotazioni()
            self.close()

    def controlla_disponibilità(self, dataselezionata, orario_premuto):
        controllore_lista_prenotazioni = ControlloreListaPrenotazioniTennis()
        for prenotazione in controllore_lista_prenotazioni.get_lista_prenotazioni_tennis1():
            if prenotazione.get_prezzo_totale == dataselezionata and prenotazione.ora == orario_premuto:
                return False
            else:
                return True