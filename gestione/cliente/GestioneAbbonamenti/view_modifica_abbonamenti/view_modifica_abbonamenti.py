from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime

class view_modifica_abbonamenti(QWidget):

    def __init__(self, controllore_abbonamento, aggiorna_lista, lista_abbonamenti, parent=None):

        super(view_modifica_abbonamenti, self).__init__(parent)
        self.controller = controllore_abbonamento
        self.aggiorna_lista = aggiorna_lista
        self.lista_abbonamenti = lista_abbonamenti

        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Yu Gothic UI Light", 16)
        self.font_label.setBold(True)

        self.font_campi = QFont("Yu Gothic UI Light", 16)

        self.label_nome = QLabel("Nome:")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.campo_nome.setFont(self.font_campi)
        self.campo_nome.setText(self.controller.get_nome_abbonamento())
        self.v_layout.addWidget(self.campo_nome)

        self.label_cognome = QLabel("Cognome:")
        self.label_cognome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cognome)

        self.campo_cognome = QLineEdit()
        self.campo_cognome.setFont(self.font_campi)
        self.campo_cognome.setText(self.controller.get_cognome_abbonamento())
        self.v_layout.addWidget(self.campo_cognome)

        self.label_nato = QLabel("Nato a:")
        self.label_nato.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nato)

        self.campo_nato = QLineEdit()
        self.campo_nato.setFont(self.font_campi)
        self.campo_nato.setText(self.controller.get_nato_abbonamento())
        self.v_layout.addWidget(self.campo_nato)

        self.label_data = QLabel("Data di nascita (gg/mm/aaaa) :")
        self.label_data.setFont(self.font_label)
        self.v_layout.addWidget(self.label_data)

        self.campo_data = QLineEdit()
        self.campo_data.setFont(self.font_campi)
        self.stringa = str(self.controller.get_data_abbonamento().strftime("%d/%m/%Y"))
        self.campo_data.setText(self.stringa)
        self.v_layout.addWidget(self.campo_data)

        self.label_residenza = QLabel("Residenza (Via e città di residenza) :")
        self.label_residenza.setFont(self.font_label)
        self.v_layout.addWidget(self.label_residenza)

        self.campo_residenza = QLineEdit()
        self.campo_residenza.setFont(self.font_campi)
        self.campo_residenza.setText((self.controller.get_residenza_abbonamento()))
        self.v_layout.addWidget(self.campo_residenza)
        self.h_layout = QHBoxLayout()

        self.label_codicefiscale = QLabel("Codice fiscale (16 caratteri):")
        self.label_codicefiscale.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codicefiscale)

        self.campo_codicefiscale = QLineEdit()
        self.campo_codicefiscale.setFont(self.font_campi)
        self.campo_codicefiscale.setText(self.controller.get_codicefiscale_abbonamento())
        self.v_layout.addWidget(self.campo_codicefiscale)

        self.label_email = QLabel("Email :")
        self.label_email.setFont(self.font_label)
        self.v_layout.addWidget(self.label_email)

        self.campo_email = QLineEdit()
        self.campo_email.setFont(self.font_campi)
        self.campo_email.setText((self.controller.get_email_abbonamento()))
        self.v_layout.addWidget(self.campo_email)
        self.h_layout = QHBoxLayout()

        self.label_cellulare = QLabel("Cellulare :")
        self.label_cellulare.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cellulare)

        self.campo_cellulare = QLineEdit()
        self.campo_cellulare.setFont(self.font_campi)
        self.campo_cellulare.setText(str(self.controller.get_cellulare_abbonamento()))
        self.v_layout.addWidget(self.campo_cellulare)
        self.h_layout = QHBoxLayout()

        self.label_struttura= QLabel("Struttura:")
        self.label_struttura.setFont(self.font_label)
        self.v_layout.addWidget(self.label_struttura)

        self.campo_struttura = QLineEdit()
        self.campo_struttura.setFont(self.font_campi)
        self.campo_struttura.setText((self.controller.get_struttura_abbonamento()))
        self.v_layout.addWidget(self.campo_struttura)
        self.h_layout = QHBoxLayout()

        self.label_tipoabbonamento = QLabel("Tipo di Abbonamento :")
        self.label_tipoabbonamento.setFont(self.font_label)
        self.v_layout.addWidget(self.label_tipoabbonamento)

        self.campo_tipoabbonamento = QComboBox(self)
        self.campo_tipoabbonamento.addItem("")
        self.campo_tipoabbonamento.addItem("settimanale")
        self.campo_tipoabbonamento.addItem("mensile")
        self.campo_tipoabbonamento.addItem("trimestrale")
        self.campo_tipoabbonamento.addItem("semestrale")
        self.campo_tipoabbonamento.addItem("annuale")

        self.v_layout.addWidget(self.campo_tipoabbonamento)

        self.campo_tipoabbonamento.setCurrentText((self.controller.get_tipoabbonamento_abbonamento()))
        self.v_layout.addWidget(self.campo_tipoabbonamento)
        self.h_layout = QHBoxLayout()


        self.bottone_chiudi = QPushButton("Chiudi")
        self.bottone_chiudi.setFont(self.font_campi)
        self.bottone_chiudi.clicked.connect(self.chiudi_finestra)
        self.bottone_chiudi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_chiudi)

        self.bottone_modifica = QPushButton("Modifica")
        self.bottone_modifica.setFont(self.font_campi)
        self.bottone_modifica.clicked.connect(self.modifica_abbonamento)
        self.bottone_modifica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_modifica)
        self.shortcut_modifica = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_modifica.activated.connect(self.modifica_abbonamento)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica abbonamento")
        self.resize(300, 400)

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 720)
        self.setMaximumSize(781, 720)
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 721))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


    def chiudi_finestra(self):
        self.close()

    def controlla_codicefiscale_libero(self, codicefiscale):

        for abbonamento in self.lista_abbonamenti:
            if abbonamento.codicefiscale == codicefiscale:
                return False
        return True

    def modifica_abbonamento(self):

        nome = self.campo_nome.text()
        cognome = self.campo_cognome.text()
        nato = self.campo_nato.text()
        data = self.campo_data.text()
        codicefiscale = self.campo_codicefiscale.text()
        residenza = self.campo_residenza.text()
        email = self.campo_email.text()
        cellulare = self.campo_cellulare.text()
        struttura = self.campo_struttura.text()
        tipoabbonamento = str(self.campo_tipoabbonamento.currentText())



        if nome == "" or cognome == "" or nato == "" or data == ""  or codicefiscale == "" or residenza == "" or email == "" or cellulare == "" or tipoabbonamento == "":

            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        if len(codicefiscale) < 16:
            QMessageBox.critical(self, "Errore", "Codice fiscale deve avere 16 caratteri", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if len(codicefiscale) > 16:
            QMessageBox.critical(self, "Errore", "Codice fiscale deve avere 16 caratteri", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if self.controller.get_codicefiscale_abbonamento() == codicefiscale:
            pass

        elif not self.controlla_codicefiscale_libero(codicefiscale):
            QMessageBox.critical(self, "Errore", "Il codice fiscale inserito è già stato utilizzato", QMessageBox.Ok,QMessageBox.Ok)
            return

        try:
            cellulare = float(self.campo_cellulare.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per il numero di cellulare", QMessageBox.Ok,QMessageBox.Ok)
            return

        try:
            nato = str(self.campo_nato.text())

        except:

            QMessageBox.critical(self, "Errore", "Inserisci solo lettere per il luogo di nascita", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            data = datetime.strptime(data,"%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci il formato della data richiesto.", QMessageBox.Ok, QMessageBox.Ok)
            return



        self.controller.set_nome_abbonamento(nome)
        self.controller.set_cognome_abbonamento(cognome)
        self.controller.set_data_abbonamento(nato)
        self.controller.set_codicefiscale_abbonamento(codicefiscale)
        self.controller.set_data_abbonamento(data)
        self.controller.set_residenza_abbonamento(residenza)
        self.controller.set_email_abbonamento(email)
        self.controller.set_cellulare_abbonamento(cellulare)
        self.controller.set_struttura_abbonamento(struttura)
        self.controller.set_tipoabbonamento_abbonamento(tipoabbonamento)

        QMessageBox.about(self, "Completata", "Modifica completata")
        self.aggiorna_lista()
        self.close()