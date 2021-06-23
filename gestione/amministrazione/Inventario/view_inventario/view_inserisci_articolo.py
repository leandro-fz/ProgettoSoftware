from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.amministrazione.GestioneInventario.model_GestioneInventario.model_GestioneInventario import GestioniInventario


class view_InserisciInventario(QWidget):

    def __init__(self, controller, aggiorna_lista, parent=None):

        super(view_InserisciInventario, self).__init__(parent)
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

        self.label_nome = QLabel("Nome")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.v_layout.addWidget(self.campo_nome)

        self.label_cognome = QLabel("Cognome")
        self.label_cognome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cognome)

        self.campo_cognome = QLineEdit()
        self.v_layout.addWidget(self.campo_cognome)

        self.label_ruolo = QLabel("Ruolo")
        self.label_ruolo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_ruolo)

        self.campo_ruolo = QLineEdit()
        self.v_layout.addWidget(self.campo_ruolo)

        self.label_id = QLabel("ID (5 numeri)")
        self.label_id.setFont(self.font_label)
        self.v_layout.addWidget(self.label_id)

        self.campo_id = QLineEdit()
        self.v_layout.addWidget(self.campo_id)

        self.label_stipendio = QLabel("Stipendio")
        self.label_stipendio.setFont(self.font_label)
        self.v_layout.addWidget(self.label_stipendio)

        self.campo_stipendio = QLineEdit()
        self.v_layout.addWidget(self.campo_stipendio)

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

        nome = self.campo_nome.text()
        cognome = self.campo_cognome.text()
        ruolo = self.campo_ruolo.text()
        id = self.campo_id.text()
        stipendio = self.campo_stipendio.text()

        if nome == "" or cognome == "" or ruolo == "" or id == "" or stipendio == "":

            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            id = int(self.campo_id.text())
        except:
            QMessageBox.critical(self, "Errore", "ID non può avere lettere", QMessageBox.Ok, QMessageBox.Ok)
            return

        if id <10000:

            QMessageBox.critical(self, "Errore", "ID deve avere almeno 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if id > 99999:

            QMessageBox.critical(self, "Errore", "ID può avere al massimo 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if not self.controlla_id_libero(id):

            QMessageBox.critical(self, "Errore", "ID già utilizzato", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            stipendio = float(self.campo_stipendio.text())
        except:

            QMessageBox.critical(self, "Errore", "Solo numeri con punto per lo stipendio", QMessageBox.Ok,QMessageBox.Ok)
            return

        if stipendio <= 0:

            QMessageBox.critical(self, "Errore", "Lo stipendio deve essere positivo", QMessageBox.Ok,QMessageBox.Ok)
            return



        self.controller.aggiungi_inventario(GestioniInventario(nome, cognome, ruolo, id, stipendio))
        self.controller.save_data()

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))
        QMessageBox.about(self, "Completato", "Inserimento completato")
        self.aggiorna_lista()
        self.close()


    def controlla_id_libero(self, id):

        for inventario in self.controller.get_lista_inventario():
            if inventario.id == id:
                return False
        return True