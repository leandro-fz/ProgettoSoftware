from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime


class view_modifica_certificati(QWidget):

    def __init__(self, controllore_certificato, aggiorna_lista, lista_certificati, parent=None):

        super(view_modifica_certificati, self).__init__(parent)
        self.controller = controllore_certificato
        self.aggiorna_lista = aggiorna_lista
        self.lista_certificati = lista_certificati

        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Yu Gothic UI Light", 16)
        self.font_label.setBold(True)

        self.font_campi = QFont("Yu Gothic UI Light", 16)


        self.create_label("Codice Fiscale:        ", self.controller.get_codicefiscale_certificato())


        self.label_sportcertificato = QLabel("Sport del certificato:")
        self.label_sportcertificato.setFont(self.font_label)
        self.v_layout.addWidget(self.label_sportcertificato)

        self.campo_sportcertificato = QLineEdit()
        self.campo_sportcertificato.setFont(self.font_campi)
        self.campo_sportcertificato.setText((self.controller.get_sportcertificato_certificato()))
        self.v_layout.addWidget(self.campo_sportcertificato)

        self.checkbox_sportcertificato = QCheckBox("Certificato agonistico")
        self.a = self.controller.get_certificatoagonistico_certificato()
        if self.a:
            self.checkbox_sportcertificato.setChecked(True)
        self.v_layout.addWidget(self.checkbox_sportcertificato)

        self.label_datainizio = QLabel("Data inizio validità certificato (gg/mm/aaaa) :")
        self.label_datainizio.setFont(self.font_label)
        self.v_layout.addWidget(self.label_datainizio)

        self.campo_datainizio = QLineEdit()
        self.campo_datainizio.setFont(self.font_campi)
        self.stringa = str(self.controller.get_datainizio_certificato().strftime("%d/%m/%Y"))
        self.campo_datainizio.setText(self.stringa)
        self.v_layout.addWidget(self.campo_datainizio)

        self.label_datafine = QLabel("Data scadenza validità certificato (gg/mm/aaaa) :")
        self.label_datafine.setFont(self.font_label)
        self.v_layout.addWidget(self.label_datafine)

        self.campo_datafine = QLineEdit()
        self.campo_datafine.setFont(self.font_campi)
        self.stringa1 = str(self.controller.get_datafine_certificato().strftime("%d/%m/%Y"))
        self.campo_datafine.setText(self.stringa1)
        self.v_layout.addWidget(self.campo_datafine)

        self.h_layout = QHBoxLayout()

        self.bottone_chiudi = QPushButton("Chiudi")
        self.bottone_chiudi.setFont(self.font_campi)
        self.bottone_chiudi.clicked.connect(self.chiudi_finestra)
        self.bottone_chiudi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_chiudi)

        self.bottone_modifica = QPushButton("Modifica")
        self.bottone_modifica.setFont(self.font_campi)
        self.bottone_modifica.clicked.connect(self.modifica_certificato)
        self.bottone_modifica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_modifica)
        self.shortcut_modifica = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_modifica.activated.connect(self.modifica_certificato)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica certificato")

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 600)
        self.setMaximumSize(781, 600)
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 601))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


    def create_label(self, testo, descrizione):
        h_layout = QHBoxLayout()

        label = QLabel(testo)
        label.setFont(QFont("Arial", 15))
        h_layout.addWidget(label)

        label_di_testo = QLabel(descrizione)
        label_di_testo.setFont(QFont("Yu Gothic UI Light", 15))
        h_layout.addWidget(label_di_testo)

        self.v_layout.addLayout(h_layout)


    # permette di chiudere la finestra di modifica del certificato
    def chiudi_finestra(self):
        self.close()

    # dopo aver compilato la modifica, l'utente preme il pulsante "modifica" e la seguente funzione controlla se tutto è stato inserito correttamente
    # e se si, salva sul file
    def modifica_certificato(self):

        sportcertificato = self.campo_sportcertificato.text()
        booleancertificato = self.a
        datainizio = self.campo_datainizio.text()
        datafine = self.campo_datafine.text()


        if self.checkbox_sportcertificato.isChecked():
            booleancertificato = True
        else:
            booleancertificato = False


        if sportcertificato == "" or datainizio == "" or datafine == "":

            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            datainizio = datetime.strptime(datainizio,"%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci il formato della data richiesto.", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            datafine = datetime.strptime(datafine,"%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci il formato della data richiesto.", QMessageBox.Ok, QMessageBox.Ok)
            return

        if datafine < datainizio:
            QMessageBox.critical(self, "Errore", "La data di scadenza non può essere precedente alla data di inizio di valdità.", QMessageBox.Ok, QMessageBox.Ok)
            return


        self.controller.set_sportcertificato_certificato(sportcertificato)
        self.controller.set_certificatoagonistico_certificato(booleancertificato)
        self.controller.set_datainizio_certificato(datainizio)
        self.controller.set_datafine_certificato(datafine)

        QMessageBox.about(self, "Completata", "Modifica completata")
        self.aggiorna_lista()
        self.close()

