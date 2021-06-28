from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime


class view_ModificaFornitore(QWidget):

    def __init__(self, controllore_fornitore, aggiorna_lista, lista_fornitori, parent=None):

        super(view_ModificaFornitore, self).__init__(parent)
        self.controller = controllore_fornitore
        self.aggiorna_lista = aggiorna_lista
        self.lista_fornitori = lista_fornitori

        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Yu Gothic UI Light", 16)
        self.font_label.setBold(True)

        self.font_campi = QFont("Yu Gothic UI Light", 16)

        self.label_ente = QLabel("Ente fornitore:")
        self.label_ente.setFont(self.font_label)
        self.v_layout.addWidget(self.label_ente)

        self.campo_ente = QLineEdit()
        self.campo_ente.setFont(self.font_campi)
        self.campo_ente.setText(self.controller.get_ente_fornitore())
        self.v_layout.addWidget(self.campo_ente)

        self.label_data = QLabel("Data spedizione ( gg/mm/aaaa) :")
        self.label_data.setFont(self.font_label)
        self.v_layout.addWidget(self.label_data)

        self.campo_data = QLineEdit()
        self.campo_data.setFont(self.font_campi)
        self.stringa = str(self.controller.get_data_fornitore().strftime("%d/%m/%Y"))
        self.campo_data.setText(self.stringa)
        self.v_layout.addWidget(self.campo_data)

        self.label_articolo = QLabel("Articolo:")
        self.label_articolo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_articolo)

        self.campo_articolo = QLineEdit()
        self.campo_articolo.setFont(self.font_campi)
        self.campo_articolo.setText(str(self.controller.get_articolo_fornitore()))
        self.v_layout.addWidget(self.campo_articolo)

        self.label_codicearticolo = QLabel("Codice articolo:")
        self.label_codicearticolo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codicearticolo)

        self.campo_codicearticolo = QLineEdit()
        self.campo_codicearticolo.setFont(self.font_campi)
        self.campo_codicearticolo.setText(str(self.controller.get_codicearticolo_fornitore()))
        self.v_layout.addWidget(self.campo_codicearticolo)

        self.label_quantita = QLabel("Quantità:")
        self.label_quantita.setFont(self.font_label)
        self.v_layout.addWidget(self.label_quantita)

        self.campo_quantita = QLineEdit()
        self.campo_quantita.setFont(self.font_campi)
        self.campo_quantita.setText(str(self.controller.get_quantita_fornitore()))
        self.v_layout.addWidget(self.campo_quantita)

        self.label_iva = QLabel("Partita IVA:")
        self.label_iva.setFont(self.font_label)
        self.v_layout.addWidget(self.label_iva)

        self.campo_iva = QLineEdit()
        self.campo_iva.setFont(self.font_campi)
        self.campo_iva.setText(str(self.controller.get_iva_fornitore()))
        self.v_layout.addWidget(self.campo_iva)

        self.h_layout = QHBoxLayout()

        self.bottone_chiudi = QPushButton("Chiudi")
        self.bottone_chiudi.setFont(self.font_campi)
        self.bottone_chiudi.clicked.connect(self.chiudi_finestra)
        self.bottone_chiudi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_chiudi)

        self.bottone_modifica = QPushButton("Modifica")
        self.bottone_modifica.setFont(self.font_campi)
        self.bottone_modifica.clicked.connect(self.modifica_fornitore)
        self.bottone_modifica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_modifica)
        self.shortcut_modifica = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_modifica.activated.connect(self.modifica_fornitore)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("fornitore")
        self.resize(300, 400)

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 590)
        self.setMaximumSize(781, 590)
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 591))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


    def chiudi_finestra(self):
        self.close()

    def controlla_id_libero(self, codicearticolo):

        for fornitore in self.lista_fornitori:
            if fornitore.codicearticolo == codicearticolo:
                return False
        return True

    def modifica_fornitore(self):

        ente = self.campo_ente.text()
        data = self.campo_data.text()
        articolo = self.campo_articolo.text()
        codicearticolo = self.campo_codicearticolo.text()
        quantita = self.campo_quantita.text()
        iva = self.campo_iva.text()


        if ente == "" or data == "" or articolo == "" or codicearticolo == "" or quantita == "" or iva == "":

            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            codicearticolo = int(self.campo_codicearticolo.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per il codice articolo", QMessageBox.Ok, QMessageBox.Ok)
            return

        if codicearticolo <10000:

            QMessageBox.critical(self, "Errore", "Il codice dell'articolo deve avere almeno 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if codicearticolo > 99999:

            QMessageBox.critical(self, "Errore", "Il codice dell'articolo  può avere al massimo 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.controller.get_codicearticolo_fornitore() == codicearticolo:
            pass

        elif not self.controlla_codicearticolo_libero(codicearticolo):
            QMessageBox.critical(self, "Errore", "Il codice dell'articolo inserito è già stato utilizzato", QMessageBox.Ok,QMessageBox.Ok)
            return

        try:
            quantita = float(self.campo_quantita.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri positivi per la quantita", QMessageBox.Ok,QMessageBox.Ok)
            return

        if quantita <= 0:

            QMessageBox.critical(self, "Errore", "La quantità non può essere negativa", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            iva = int(self.campo_iva.text())
        except:
            QMessageBox.critical(self, "Errore", "La Partita IVA non può avere lettere", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            data = datetime.strptime(data,"%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci il formato della data richiesto.", QMessageBox.Ok, QMessageBox.Ok)
            return

        # if ente == "" or data == "" or articolo == "" or id == 0 or quantita == 0.0:
        #
        #     QMessageBox.critical(self, "Errore", "Completa tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
        #     return

        self.controller.set_ente_fornitore(ente)
        self.controller.set_data_fornitore(data)
        self.controller.set_articolo_fornitore(articolo)
        self.controller.set_codicearticolo_fornitore(codicearticolo)
        self.controller.set_quantita_fornitore(quantita)
        self.controller.set_iva_fornitore(iva)
        QMessageBox.about(self, "Completata", "Modifica completata")
        self.aggiorna_lista()
        self.close()