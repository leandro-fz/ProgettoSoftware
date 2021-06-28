from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime

from gestione.amministrazione.GestioneFornitori.model_GestioneFornitori.model_GestioneFornitori import GestioniFornitore


class view_InserisciFornitore(QWidget):

    def __init__(self, controller, aggiorna_lista, parent=None):

        super(view_InserisciFornitore, self).__init__(parent)
        self.controller = controller
        self.aggiorna_lista = aggiorna_lista

        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Yu Gothic UI Light", 15)
        self.font_label.setBold(True)


        self.font_label2 = QFont("Yu Gothic UI Light", 20)
        self.label_alto = QLabel("Compila il form di inserimento del fornitore")
        self.label_alto.setFont(self.font_label2)
        self.v_layout.addWidget(self.label_alto)

        # self.v_layout.addSpacing(10)

        self.label_ente = QLabel("Ente fornitore: ")
        self.label_ente.setFont(self.font_label)
        self.v_layout.addWidget(self.label_ente)

        self.campo_ente = QLineEdit()
        self.v_layout.addWidget(self.campo_ente)

        self.label_data = QLabel("Data spedizione (gg/mm/aaaa)")
        self.label_data.setFont(self.font_label)
        self.v_layout.addWidget(self.label_data)

        self.campo_data = QLineEdit()
        self.v_layout.addWidget(self.campo_data)

        self.label_articolo = QLabel("Articolo:")
        self.label_articolo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_articolo)

        self.campo_articolo = QLineEdit()
        self.v_layout.addWidget(self.campo_articolo)

        self.label_codicearticolo = QLabel("Codice articolo:")
        self.label_codicearticolo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codicearticolo)

        self.campo_codicearticolo = QLineEdit()
        self.v_layout.addWidget(self.campo_codicearticolo)

        self.label_quantita = QLabel("Quantità : ")
        self.label_quantita.setFont(self.font_label)
        self.v_layout.addWidget(self.label_quantita)

        self.campo_quantita = QLineEdit()
        self.v_layout.addWidget(self.campo_quantita)

        self.label_iva = QLabel("Partita IVA (11 caratteri):")
        self.label_iva.setFont(self.font_label)
        self.v_layout.addWidget(self.label_iva)

        self.campo_iva= QLineEdit()
        self.v_layout.addWidget(self.campo_iva)

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
        self.setWindowTitle("Inserimento fornitore")
        self.resize(300, 400)

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 590)
        self.setMaximumSize(781, 590)

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 591))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    def mostra_annulla_ins(self):
        reply = QMessageBox.question(self, 'Annullare', 'Sei sicuro di voler uscire?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass


    def conferma_inserimento(self):

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
            QMessageBox.critical(self, "Errore", "Il codice dell'articolo non può avere lettere", QMessageBox.Ok, QMessageBox.Ok)
            return


        if codicearticolo <10000:

            QMessageBox.critical(self, "Errore", "Il codice dell'articolo deve avere almeno 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if codicearticolo > 99999:

            QMessageBox.critical(self, "Errore", "Il codice dell'articolo può avere al massimo 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if not self.controlla_codicearticolo_libero(codicearticolo):

            QMessageBox.critical(self, "Errore", "Codice dell'articolo già utilizzato", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            iva = int(self.campo_iva.text())
        except:
            QMessageBox.critical(self, "Errore", "La Partita IVA non può avere lettere", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            quantita = float(self.campo_quantita.text())
        except:

            QMessageBox.critical(self, "Errore", "Solo numeri positivi per la quantita", QMessageBox.Ok,QMessageBox.Ok)
            return

        if quantita <= 0:

            QMessageBox.critical(self, "Errore", "La quantità deve essere positiva", QMessageBox.Ok,QMessageBox.Ok)
            return

        try:
            data = datetime.strptime(data,"%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci il formato della data richiesto", QMessageBox.Ok, QMessageBox.Ok)
            return


        self.controller.aggiungi_fornitore(GestioniFornitore(ente, data, articolo, codicearticolo, quantita,iva ))
        self.controller.save_data()

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))
        QMessageBox.about(self, "Completato", "Inserimento completato")
        self.aggiorna_lista()
        self.close()


    def controlla_codicearticolo_libero(self, codicearticolo):

        for fornitore in self.controller.get_lista_fornitori():
            if fornitore.codicearticolo == codicearticolo:
                return False
        return True