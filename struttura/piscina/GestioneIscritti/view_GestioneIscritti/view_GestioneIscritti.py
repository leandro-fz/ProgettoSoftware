from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class view_ModificaUtente(QWidget):

    def __init__(self, controllore_utente, aggiorna_lista, lista_iscritti, parent=None):

        super(view_ModificaUtente, self).__init__(parent)
        self.controller = controllore_utente
        self.aggiorna_lista = aggiorna_lista
        self.lista_iscritti = lista_iscritti

        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Yu Gothic UI Light", 16)
        self.font_label.setBold(True)

        self.font_campi = QFont("Yu Gothic UI Light", 16)

        self.label_nome = QLabel("Nome:")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.campo_nome.setFont(self.font_campi)
        self.campo_nome.setText(self.controller.get_nome_utente())
        self.v_layout.addWidget(self.campo_nome)

        self.label_cognome = QLabel("Cognome:")
        self.label_cognome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cognome)

        self.campo_cognome = QLineEdit()
        self.campo_cognome.setFont(self.font_campi)
        self.campo_cognome.setText(self.controller.get_cognome_utente())
        self.v_layout.addWidget(self.campo_cognome)


        self.label_codicefiscale = QLabel("Codice Fiscale:")
        self.label_codicefiscale.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codicefiscale)

        self.campo_codicefiscale = QLineEdit()
        self.campo_codicefiscale.setFont(self.font_campi)
        self.campo_codicefiscale.setText(str(self.controller.get_codicefiscale_utente()))
        self.v_layout.addWidget(self.campo_codicefiscale)

        self.label_cellulare = QLabel("Cellulare :")
        self.label_cellulare.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cellulare)

        self.campo_cellulare = QLineEdit()
        self.campo_cellulare.setFont(self.font_campi)
        self.campo_cellulare.setText(str(self.controller.get_cellulare_utente()))
        self.v_layout.addWidget(self.campo_cellulare)
        self.h_layout = QHBoxLayout()

        self.label_certificato = QLabel("Certificato:")
        self.label_certificato.setFont(self.font_label)
        self.v_layout.addWidget(self.label_certificato)

        self.campo_certificato = QLineEdit()
        self.campo_certificato.setFont(self.font_campi)
        self.campo_certificato.setText(self.controller.get_certificato_utente())
        self.v_layout.addWidget(self.campo_certificato)

        self.checkbox_certificato = QCheckBox("Certificato agonistico")
        self.a = self.controller.get_certificatoagonistico_utente
        if self.a:
            self.checkbox_certificato.setChecked(True)
        self.v_layout.addWidget(self.checkbox_certificato)

        self.label_tipoabbonamento= QLabel("Tipo abbonamento:")
        self.label_tipoabbonamento.setFont(self.font_label)
        self.v_layout.addWidget(self.label_tipoabbonamento)

        self.campo_tipoabbonamento = QLineEdit()
        self.campo_tipoabbonamento.setFont(self.font_campi)
        self.campo_tipoabbonamento.setText(self.controller.get_tipoabbonamento_utente())
        self.v_layout.addWidget(self.campo_tipoabbonamento)

        self.h_layout = QHBoxLayout()

        self.bottone_chiudi = QPushButton("Chiudi")
        self.bottone_chiudi.setFont(self.font_campi)
        self.bottone_chiudi.clicked.connect(self.chiudi_finestra)
        self.bottone_chiudi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_chiudi)

        self.bottone_modifica = QPushButton("Modifica")
        self.bottone_modifica.setFont(self.font_campi)
        self.bottone_modifica.clicked.connect(self.modifica_utente)
        self.bottone_modifica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_modifica)
        self.shortcut_modifica = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_modifica.activated.connect(self.modifica_utente)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("utente")
        self.resize(300, 400)

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

        for utente in self.lista_iscritti:
            if utente.codicefiscale == codicefiscale:
                return False
        return True

    def modifica_utente(self):

        nome = self.campo_nome.text()
        cognome = self.campo_cognome.text()
        codicefiscale = self.campo_codicefiscale.text()
        cellulare = self.campo_cellulare.text()
        certificato = self.campo_certificato.text()
        booleancertificato = self.a
        tipoabbonamento = self.campo_tipoabbonamento.text()

        if self.checkbox_certificato.isChecked():
            booleancertificato = True
            print("ok")
        else:
            booleancertificato = False
            print("ok")
            print("ok")

        if nome == "" or cognome == ""  or codicefiscale == "" or cellulare == "" or certificato == "" or tipoabbonamento == "":
            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            codicefiscale = int(self.campo_codicefiscale.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per il codice fiscale", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if codicefiscale < 10000:
            QMessageBox.critical(self, "Errore", "Il codice fiscale deve avere almeno 5 cifre", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if codicefiscale > 99999:
            QMessageBox.critical(self, "Errore", "Il codice fiscale può avere al massimo 5 cifre", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if self.controller.get_codicefiscale_utente() == codicefiscale:
            pass

        elif not self.controlla_codicefiscale_libero(codicefiscale):
            QMessageBox.critical(self, "Errore", "Il codice fiscale inserito è già stato utilizzato", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        try:
            cellulare = int(self.campo_cellulare.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per il numero di cellulare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        # if nome == "" or cognome == "" or ruolo == "" or id == 0 or stipendio == 0.0:
        #
        #     QMessageBox.critical(self, "Errore", "Completa tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
        #     return

        self.controller.set_nome_utente(nome)
        self.controller.set_cognome_utente(cognome)
        self.controller.set_tipoabbonamento_utente(tipoabbonamento)
        self.controller.set_codicefiscale_utente(codicefiscale)
        self.controller.set_certificato_utente(certificato)
        self.controller.set_certificatoagonistico_utente(booleancertificato)
        self.controller.set_cellulare_utente(cellulare)

        QMessageBox.about(self, "Completata", "Modifica completata")
        self.aggiorna_lista()
        self.close()