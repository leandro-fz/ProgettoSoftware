from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.amministrazione.dipendenti.controller_dipendenti.controller_dipendenti import Controller_Dipendenti
from gestione.amministrazione.GestioneDipendenti.model_GestioneDipendenti.model_GestioneDipendenti import GestioniDipendente


class view_InserisciDipendente(QWidget):

    def __init__(self, controller, aggiorna_lista, parent=None):

        super(view_InserisciDipendente, self).__init__(parent)
        self.controller = controller
        self.aggiorna_lista = aggiorna_lista

        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Yu Gothic UI Light", 14)
        self.font_label.setBold(True)


        self.font_label2 = QFont("Yu Gothic UI Light", 18)
        self.label_alto = QLabel("Compila il form di inserimento del dipendente")
        self.label_alto.setFont(self.font_label2)
        self.v_layout.addWidget(self.label_alto)

        # self.v_layout.addSpacing(10)

        self.label_nome = QLabel("Nome: ")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.v_layout.addWidget(self.campo_nome)

        self.label_cognome = QLabel("Cognome: ")
        self.label_cognome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cognome)

        self.campo_cognome = QLineEdit()
        self.v_layout.addWidget(self.campo_cognome)

        self.label_ruolo = QLabel("Ruolo: ")
        self.label_ruolo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_ruolo)

        self.campo_ruolo = QLineEdit()
        self.v_layout.addWidget(self.campo_ruolo)

        self.label_luogo = QLabel("Luogo di nascita: ")
        self.label_luogo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_luogo)

        self.campo_luogo = QLineEdit()
        self.v_layout.addWidget(self.campo_luogo)

        self.label_data = QLabel("Data di nascita (gg/mm/aaaa): ")
        self.label_data.setFont(self.font_label)
        self.v_layout.addWidget(self.label_data)

        self.campo_data = QLineEdit()
        self.v_layout.addWidget(self.campo_data)

        self.label_codice = QLabel("Codice fiscale:")
        self.label_codice.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codice)

        self.campo_codice = QLineEdit()
        self.v_layout.addWidget(self.campo_codice)

        self.label_contratto = QLabel("Tipo di contratto:")
        self.label_contratto.setFont(self.font_label)
        self.v_layout.addWidget(self.label_contratto)

        self.campo_contratto = QLineEdit()
        self.v_layout.addWidget(self.campo_contratto)


        self.label_id = QLabel("ID (5 numeri): ")
        self.label_id.setFont(self.font_label)
        self.v_layout.addWidget(self.label_id)

        self.campo_id = QLineEdit()
        self.v_layout.addWidget(self.campo_id)

        self.label_stipendio = QLabel("Stipendio: ")
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
        self.setWindowTitle("Inserimento Dipendente")
        self.resize(300, 400)

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 610)
        self.setMaximumSize(781, 610)

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 611))
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
        luogo = self.campo_luogo.text()
        data = self.campo_data.text()
        codice = self.campo_codice.text()
        contratto = self.campo_contratto.text()
        ruolo = self.campo_ruolo.text()
        id = self.campo_id.text()
        stipendio = self.campo_stipendio.text()

        if nome == "" or cognome == "" or luogo == "" or data == " " or codice == " " or contratto == "" or ruolo == "" or id == "" or stipendio == "":

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

        try:
            data = datetime.strptime(data,"%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci il formato della data richiesto", QMessageBox.Ok, QMessageBox.Ok)
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



        self.controller.aggiungi_dipendente(GestioniDipendente(nome, cognome, luogo, data, codice, contratto, ruolo, id, stipendio))
        self.controller.save_data()

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))
        QMessageBox.about(self, "Completato", "Inserimento completato")
        self.aggiorna_lista()
        self.close()


    def controlla_id_libero(self, id):

        for dipendente in self.controller.get_lista_dipendenti():
            if dipendente.id == id:
                return False
        return True