from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class view_ModificaDipendente(QWidget):

    def __init__(self, controllore_dipendente, aggiorna_lista, lista_dipendenti, parent=None):

        super(view_ModificaDipendente, self).__init__(parent)
        self.controller = controllore_dipendente
        self.aggiorna_lista = aggiorna_lista
        self.lista_dipendenti = lista_dipendenti

        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Yu Gothic UI Light", 14)
        self.font_label.setBold(True)

        self.font_campi = QFont("Yu Gothic UI Light", 14)

        self.label_nome = QLabel("Nome:")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.campo_nome.setFont(self.font_campi)
        self.campo_nome.setText(self.controller.get_nome_dipendente())
        self.v_layout.addWidget(self.campo_nome)

        self.label_cognome = QLabel("Cognome:")
        self.label_cognome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cognome)

        self.campo_cognome = QLineEdit()
        self.campo_cognome.setFont(self.font_campi)
        self.campo_cognome.setText(self.controller.get_cognome_dipendente())
        self.v_layout.addWidget(self.campo_cognome)

        self.label_luogo = QLabel("Luogo di nascita:")
        self.label_luogo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_luogo)

        self.campo_luogo = QLineEdit()
        self.campo_luogo.setFont(self.font_campi)
        self.campo_luogo.setText(self.controller.get_luogo_dipendente())
        self.v_layout.addWidget(self.campo_luogo)

        self.label_data = QLabel("Data di nascita (gg/mm/aaaa):")
        self.label_data.setFont(self.font_label)
        self.v_layout.addWidget(self.label_data)

        self.campo_data = QLineEdit()
        self.campo_data.setFont(self.font_campi)
        self.stringa = str(self.controller.get_data_dipendente().strftime("%d/%m/%Y"))
        self.campo_data.setText(self.stringa)
        self.v_layout.addWidget(self.campo_data)

        self.label_codice = QLabel("Codice fiscale:")
        self.label_codice.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codice)

        self.campo_codice = QLineEdit()
        self.campo_codice.setFont(self.font_campi)
        self.campo_codice.setText(self.controller.get_codice_dipendente())
        self.v_layout.addWidget(self.campo_codice)

        self.label_contratto = QLabel("Tipo di contratto:")
        self.label_contratto.setFont(self.font_label)
        self.v_layout.addWidget(self.label_contratto)

        self.campo_contratto = QLineEdit()
        self.campo_contratto.setFont(self.font_campi)
        self.campo_contratto.setText(self.controller.get_contratto_dipendente())
        self.v_layout.addWidget(self.campo_contratto)

        self.label_ruolo = QLabel("Ruolo:")
        self.label_ruolo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_ruolo)

        self.campo_ruolo = QLineEdit()
        self.campo_ruolo.setFont(self.font_campi)
        self.campo_ruolo.setText(self.controller.get_ruolo_dipendente())
        self.v_layout.addWidget(self.campo_ruolo)

        self.label_id = QLabel("ID:")
        self.label_id.setFont(self.font_label)
        self.v_layout.addWidget(self.label_id)

        self.campo_id = QLineEdit()
        self.campo_id.setFont(self.font_campi)
        self.campo_id.setText(str(self.controller.get_id_dipendente()))
        self.v_layout.addWidget(self.campo_id)

        self.label_stipendio = QLabel("Stipendio:")
        self.label_stipendio.setFont(self.font_label)
        self.v_layout.addWidget(self.label_stipendio)

        self.campo_stipendio = QLineEdit()
        self.campo_stipendio.setFont(self.font_campi)
        self.campo_stipendio.setText(str(self.controller.get_stipendio_dipendente()))
        self.v_layout.addWidget(self.campo_stipendio)

        self.h_layout = QHBoxLayout()

        self.bottone_chiudi = QPushButton("Chiudi")
        self.bottone_chiudi.setFont(self.font_campi)
        self.bottone_chiudi.clicked.connect(self.chiudi_finestra)
        self.bottone_chiudi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_chiudi)

        self.bottone_modifica = QPushButton("Modifica")
        self.bottone_modifica.setFont(self.font_campi)
        self.bottone_modifica.clicked.connect(self.modifica_dipendente)
        self.bottone_modifica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_modifica)
        self.shortcut_modifica = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_modifica.activated.connect(self.modifica_dipendente)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dipendente")
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

    def controlla_id_libero(self, id):

        for dipendente in self.lista_dipendenti:
            if dipendente.id == id:
                return False
        return True

    def modifica_dipendente(self):

        nome = self.campo_nome.text()
        cognome = self.campo_cognome.text()
        luogo = self.campo_luogo.text()
        data = self.campo_data.text()
        codice = self.campo_codice.text()
        contratto = self.campo_contratto.text()
        ruolo = self.campo_ruolo.text()
        id = self.campo_id.text()
        stipendio = self.campo_stipendio.text()

        if nome == "" or cognome == "" or luogo == "" or data == "" or codice == "" or contratto == " " or ruolo == "" or id == "" or stipendio == "":

            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            id = int(self.campo_id.text())

        except:

            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per il codice ID", QMessageBox.Ok, QMessageBox.Ok)
            return

        if id <10000:

            QMessageBox.critical(self, "Errore", "ID deve avere almeno 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if id > 99999:

            QMessageBox.critical(self, "Errore", "ID può avere al massimo 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.controller.get_id_dipendente() == id:
            pass

        elif not self.controlla_id_libero(id):
            QMessageBox.critical(self, "Errore", "L'ID inserito è già stato utilizzato", QMessageBox.Ok,QMessageBox.Ok)
            return

        try:
            stipendio = float(self.campo_stipendio.text())

        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri con il punto per lo stipendio", QMessageBox.Ok,QMessageBox.Ok)
            return

        if stipendio <= 0:

            QMessageBox.critical(self, "Errore", "Lo stipendio non può essere negativo", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            data = datetime.strptime(data, "%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci il formato della data richiesto", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        # if nome == "" or cognome == "" or ruolo == "" or id == 0 or stipendio == 0.0:
        #
        #     QMessageBox.critical(self, "Errore", "Completa tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
        #     return

        self.controller.set_nome_dipendente(nome)
        self.controller.set_cognome_dipendente(cognome)
        self.controller.set_luogo_dipendente(luogo)
        self.controller.set_data_dipendente(data)
        self.controller.set_codice_dipendente(codice)
        self.controller.set_contratto_dipendente(contratto)
        self.controller.set_ruolo_dipendente(ruolo)
        self.controller.set_id_dipendente(id)
        self.controller.set_stipendio_dipendente(stipendio)
        QMessageBox.about(self, "Completata", "Modifica completata")
        self.aggiorna_lista()
        self.close()