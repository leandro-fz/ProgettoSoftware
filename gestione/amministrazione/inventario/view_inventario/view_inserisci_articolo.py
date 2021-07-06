from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.amministrazione.GestioneInventario.model_GestioneInventario.model_GestioneInventario import GestioniInventario


class view_InserisciArticolo(QWidget):

    def __init__(self, controller, aggiorna_lista, parent=None):

        super(view_InserisciArticolo, self).__init__(parent)
        self.controller = controller
        self.aggiorna_lista = aggiorna_lista

        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Yu Gothic UI Light", 15)
        self.font_label.setBold(True)


        self.font_label2 = QFont("Yu Gothic UI Light", 20)
        self.label_alto = QLabel("Compila il form di inserimento dell'articolo")
        self.label_alto.setFont(self.font_label2)
        self.v_layout.addWidget(self.label_alto)

        # self.v_layout.addSpacing(10)

        self.label_articolo = QLabel("Articolo: ")
        self.label_articolo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_articolo)

        self.campo_articolo = QLineEdit()
        self.v_layout.addWidget(self.campo_articolo)


        self.label_quantita = QLabel("Quantità: ")
        self.label_quantita.setFont(self.font_label)
        self.v_layout.addWidget(self.label_quantita)

        self.campo_quantita = QLineEdit()
        self.v_layout.addWidget(self.campo_quantita)

        self.label_codice= QLabel("Codice articolo: ")
        self.label_codice.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codice)

        self.campo_codice = QLineEdit()
        self.v_layout.addWidget(self.campo_codice)

        self.label_prezzo = QLabel("Prezzo: ")
        self.label_prezzo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_prezzo)

        self.campo_prezzo = QLineEdit()
        self.v_layout.addWidget(self.campo_prezzo)

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
        self.setWindowTitle("Inserimento articolo")
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
        reply = QMessageBox.question(self, 'Annullare', 'Sei sicuro di voler uscire?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass


    def conferma_inserimento(self):

        articolo = self.campo_articolo.text()
        quantita = self.campo_quantita.text()
        codice = self.campo_codice.text()
        prezzo = self.campo_prezzo.text()

        if articolo == "" or quantita == "" or codice == "" or prezzo == "":

            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            codice = int(self.campo_codice.text())
        except:

            QMessageBox.critical(self, "Errore", "Il codice non può avere lettere", QMessageBox.Ok, QMessageBox.Ok)
            return

        if codice <10000:

            QMessageBox.critical(self, "Errore", "Il codice deve avere almeno 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if codice > 99999:

            QMessageBox.critical(self, "Errore", "Il codice può avere al massimo 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if not self.controlla_codice_libero(codice):

            QMessageBox.critical(self, "Errore", "Articolo già inserito. Modifica la quantità.", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            prezzo = float(self.campo_prezzo.text())

        except:

            QMessageBox.critical(self, "Errore", "Solo numeri con punto per il prezzo", QMessageBox.Ok,QMessageBox.Ok)
            return


        if prezzo <= 0:

            QMessageBox.critical(self, "Errore", "Il prezzo dell'articolo deve essere positivo", QMessageBox.Ok,QMessageBox.Ok)
            return


        self.controller.aggiungi_inventario(GestioniInventario(articolo,quantita, codice, prezzo))
        self.controller.save_data()

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))
        QMessageBox.about(self, "Completato", "Inserimento completato")
        self.aggiorna_lista()
        self.close()


    def controlla_codice_libero(self, codice):

        for inventario in self.controller.get_lista_inventario():
            if inventario.codice == codice:
                return False
        return True