from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.amministrazione.GestioneFornitori.model_gestione_fornitori.model_gestione_fornitori import model_gestione_fornitori


class view_inserisci_fornitori(QWidget):

    #view di inserisci fornitore che si occupa dell'inserimento di tutti i campi da inserire
    def __init__(self, controller, aggiorna_lista, parent=None):

        super(view_inserisci_fornitori, self).__init__(parent)
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

        self.label_nome = QLabel("Nome azienda : ")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.v_layout.addWidget(self.campo_nome)

        self.label_indirizzo = QLabel("Indirizzo: ")
        self.label_indirizzo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_indirizzo)

        self.campo_indirizzo = QLineEdit()
        self.v_layout.addWidget(self.campo_indirizzo)

        self.label_citta = QLabel("Città:")
        self.label_citta.setFont(self.font_label)
        self.v_layout.addWidget(self.label_citta)

        self.campo_citta = QLineEdit()
        self.v_layout.addWidget(self.campo_citta)

        self.label_email = QLabel("Email:")
        self.label_email.setFont(self.font_label)
        self.v_layout.addWidget(self.label_email)

        self.campo_email = QLineEdit()
        self.v_layout.addWidget(self.campo_email)

        self.label_cellulare = QLabel("Recapito telefonico : ")
        self.label_cellulare.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cellulare)

        self.campo_cellulare = QLineEdit()
        self.v_layout.addWidget(self.campo_cellulare)

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
        self.shortcut_conferma = QShortcut(QKeySequence('nomer'), self)
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

    # la funzione chiude la pagina senza inserire il fornitore
    def mostra_annulla_ins(self):
        reply = QMessageBox.question(self, 'Annullare', 'Sei sicuro di voler uscire?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass

    # la funzione salva il fornitore inserito e controlla se tutti i campi sono stati inseriti correttamente
    def conferma_inserimento(self):

        nome = self.campo_nome.text()
        indirizzo = self.campo_indirizzo.text()
        citta = self.campo_citta.text()
        email = self.campo_email.text()
        cellulare = self.campo_cellulare.text()
        iva = self.campo_iva.text()


        if nome == "" or indirizzo == "" or citta == "" or email == "" or cellulare == "" or iva == "":

            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            iva = str(int(self.campo_iva.text()))
        except:
            QMessageBox.critical(self, "Errore", "La Partita IVA non può avere lettere", QMessageBox.Ok, QMessageBox.Ok)
            return

        if len(iva) < 11:
            QMessageBox.critical(self, "Errore", "La Partita IVA deve avere 11 caratteri", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if len(iva) > 11:
            QMessageBox.critical(self, "Errore", "La Partita IVA deve avere 11 caratteri", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if not self.controlla_iva_libero(iva):

            QMessageBox.critical(self, "Errore", "Partita IVA già utilizzata", QMessageBox.Ok, QMessageBox.Ok)
            return


        try:
            cellulare = float(self.campo_cellulare.text())
        except:

            QMessageBox.critical(self, "Errore", "Solo numeri positivi per il cellulare", QMessageBox.Ok,QMessageBox.Ok)
            return



        self.controller.aggiungi_fornitore(model_gestione_fornitori(nome, indirizzo, citta, email, cellulare,iva ))
        self.controller.save_data()

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))
        QMessageBox.about(self, "Completato", "Inserimento completato")
        self.aggiorna_lista()
        self.close()

    # la funzione controlla se il campo "iva" inserito sia stato già utilizzato
    def controlla_iva_libero(self, iva):

        for fornitore in self.controller.get_lista_fornitori():
            if fornitore.iva == iva:
                return False
        return True