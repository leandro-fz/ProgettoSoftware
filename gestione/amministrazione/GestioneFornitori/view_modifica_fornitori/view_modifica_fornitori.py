from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class view_modifica_fornitori(QWidget):

    def __init__(self, controllore_fornitore, aggiorna_lista, lista_fornitori, parent=None):

        super(view_modifica_fornitori, self).__init__(parent)
        self.controller = controllore_fornitore
        self.aggiorna_lista = aggiorna_lista
        self.lista_fornitori = lista_fornitori

        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Yu Gothic UI Light", 16)
        self.font_label.setBold(True)

        self.font_campi = QFont("Yu Gothic UI Light", 16)

        self.label_nome = QLabel("Nome azienda:")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.campo_nome.setFont(self.font_campi)
        self.campo_nome.setText(self.controller.get_nome_fornitore())
        self.v_layout.addWidget(self.campo_nome)

        self.label_indirizzo = QLabel("Indirizzo :")
        self.label_indirizzo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_indirizzo)

        self.campo_indirizzo = QLineEdit()
        self.campo_indirizzo.setFont(self.font_campi)
        self.campo_indirizzo.setText(self.controller.get_indirizzo_fornitore())
        self.v_layout.addWidget(self.campo_indirizzo)

        self.label_citta = QLabel("Città:")
        self.label_citta.setFont(self.font_label)
        self.v_layout.addWidget(self.label_citta)

        self.campo_citta = QLineEdit()
        self.campo_citta.setFont(self.font_campi)
        self.campo_citta.setText(self.controller.get_citta_fornitore())
        self.v_layout.addWidget(self.campo_citta)

        self.label_email = QLabel("Email:")
        self.label_email.setFont(self.font_label)
        self.v_layout.addWidget(self.label_email)

        self.campo_email = QLineEdit()
        self.campo_email.setFont(self.font_campi)
        self.campo_email.setText(self.controller.get_email_fornitore())
        self.v_layout.addWidget(self.campo_email)

        self.label_cellulare = QLabel("Recapito telefonico: ")
        self.label_cellulare.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cellulare)

        self.campo_cellulare = QLineEdit()
        self.campo_cellulare.setFont(self.font_campi)
        self.campo_cellulare.setText(str(self.controller.get_cellulare_fornitore()))
        self.v_layout.addWidget(self.campo_cellulare)

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
        self.shortcut_modifica = QShortcut(QKeySequence('nomer'), self)
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

    def controlla_email_libero(self, email):

        for fornitore in self.lista_fornitori:
            if fornitore.email == email:
                return False
        return True

    def modifica_fornitore(self):

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

        if self.controller.get_iva_fornitore() == iva:
            pass

        elif not self.controlla_iva_libero(iva):
            QMessageBox.critical(self, "Errore", "La Partita IVA inserita è già stato utilizzata", QMessageBox.Ok,QMessageBox.Ok)
            return

        try:
            cellulare = float(self.campo_cellulare.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri positivi per la cellulare", QMessageBox.Ok,QMessageBox.Ok)
            return


        # if nome == "" or indirizzo == "" or citta == "" or id == 0 or cellulare == 0.0:
        #
        #     QMessageBox.critical(self, "Errore", "Completa tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
        #     return

        self.controller.set_nome_fornitore(nome)
        self.controller.set_indirizzo_fornitore(indirizzo)
        self.controller.set_citta_fornitore(citta)
        self.controller.set_email_fornitore(email)
        self.controller.set_cellulare_fornitore(cellulare)
        self.controller.set_iva_fornitore(iva)
        QMessageBox.about(self, "Completata", "Modifica completata")
        self.aggiorna_lista()
        self.close()