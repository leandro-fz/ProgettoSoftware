from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime

class view_ModificaCertificato(QWidget):

    def __init__(self, controllore_certificato, aggiorna_lista, lista_certificati, parent=None):

        super(view_ModificaCertificato, self).__init__(parent)
        self.controller = controllore_certificato
        self.aggiorna_lista = aggiorna_lista
        self.lista_certificati = lista_certificati

        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Yu Gothic UI Light", 16)
        self.font_label.setBold(True)

        self.font_campi = QFont("Yu Gothic UI Light", 16)

        self.label_nome = QLabel("Nome:")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.campo_nome.setFont(self.font_campi)
        self.campo_nome.setText(self.controller.get_nome_certificato())
        self.v_layout.addWidget(self.campo_nome)

        self.label_cognome = QLabel("Cognome:")
        self.label_cognome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cognome)

        self.campo_cognome = QLineEdit()
        self.campo_cognome.setFont(self.font_campi)
        self.campo_cognome.setText(self.controller.get_cognome_certificato())
        self.v_layout.addWidget(self.campo_cognome)

        self.label_nato = QLabel("Nato a:")
        self.label_nato.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nato)

        self.campo_nato = QLineEdit()
        self.campo_nato.setFont(self.font_campi)
        self.campo_nato.setText(self.controller.get_nato_certificato())
        self.v_layout.addWidget(self.campo_nato)

        self.label_codicefiscale = QLabel("Codice Fiscale:")
        self.label_codicefiscale.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codicefiscale)

        self.campo_codicefiscale = QLineEdit()
        self.campo_codicefiscale.setFont(self.font_campi)
        self.campo_codicefiscale.setText(str(self.controller.get_codicefiscale_certificato()))
        self.v_layout.addWidget(self.campo_codicefiscale)

        self.label_residenza = QLabel("Residenza (Via e città di residenza) :")
        self.label_residenza.setFont(self.font_label)
        self.v_layout.addWidget(self.label_residenza)

        self.campo_residenza = QLineEdit()
        self.campo_residenza.setFont(self.font_campi)
        self.campo_residenza.setText((self.controller.get_residenza_certificato()))
        self.v_layout.addWidget(self.campo_residenza)

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


    def chiudi_finestra(self):
        self.close()

    def controlla_codicefiscale_libero(self, codicefiscale):

        for certificato in self.lista_certificati:
            if certificato.codicefiscale == codicefiscale:
                return False
        return True

    def modifica_certificato(self):

        nome = self.campo_nome.text()
        cognome = self.campo_cognome.text()
        nato = self.campo_nato.text()
        codicefiscale = self.campo_codicefiscale.text()
        residenza = self.campo_residenza.text()
        sportcertificato = self.campo_sportcertificato.text()
        booleancertificato = self.a
        datainizio = self.campo_datainizio.text()
        datafine = self.campo_datafine.text()


        if self.checkbox_sportcertificato.isChecked():
            booleancertificato = True
        else:
            booleancertificato = False


        if nome == "" or cognome == "" or nato == "" or codicefiscale == "" or residenza == "" or sportcertificato == "" or datainizio == "" or datafine == "":

            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            codicefiscale = int(self.campo_codicefiscale.text())
        except:
            QMessageBox.critical(self, "Errore", "Codice Fiscale non può avere lettere", QMessageBox.Ok, QMessageBox.Ok)
            return
        if codicefiscale <10000:

            QMessageBox.critical(self, "Errore", "Codice fiscale deve avere almeno 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if codicefiscale > 99999:

            QMessageBox.critical(self, "Errore", "Codice fiscale può avere al massimo 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.controller.get_codicefiscale_certificato() == codicefiscale:
            pass

        elif not self.controlla_codicefiscale_libero(codicefiscale):
            QMessageBox.critical(self, "Errore", "Il codice fiscale inserito è già stato utilizzato", QMessageBox.Ok, QMessageBox.Ok)
            return


        try:
            nato = str(self.campo_nato.text())

        except:

            QMessageBox.critical(self, "Errore", "Inserisci solo lettere per il luogo di nascita", QMessageBox.Ok, QMessageBox.Ok)
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


        # if nome == "" or cognome == "" or ruolo == "" or id == 0 or stipendio == 0.0:
        #
        #     QMessageBox.critical(self, "Errore", "Completa tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
        #     return

        self.controller.set_nome_certificato(nome)
        self.controller.set_cognome_certificato(cognome)
        self.controller.set_nato_certificato(nato)
        self.controller.set_codicefiscale_certificato(codicefiscale)
        self.controller.set_residenza_certificato(residenza)
        self.controller.set_sportcertificato_certificato(sportcertificato)
        self.controller.set_certificatoagonistico_certificato(booleancertificato)
        self.controller.set_datainizio_certificato(datainizio)
        self.controller.set_datafine_certificato(datafine)

        QMessageBox.about(self, "Completata", "Modifica completata")
        self.aggiorna_lista()
        self.close()