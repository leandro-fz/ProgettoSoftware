
from PyQt5 import QtGui, QtCore

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime

from gestione.cliente.GestioneAbbonamenti.model_gestione_abbonamenti.model_gestione_abbonamenti import \
    model_gestione_abbonamenti
from gestione.cliente.abbonamenti.controller_abbonamenti.controller_abbonamenti import controller_abbonamenti



class view_inserisci_abbonamenti(QWidget):

    def __init__(self, controller, aggiorna_lista, parent=None):

        super(view_inserisci_abbonamenti, self).__init__(parent)
        self.controller = controller
        self.aggiorna_lista = aggiorna_lista

        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Yu Gothic UI Light", 15)
        self.font_label.setBold(True)


        self.font_label2 = QFont("Yu Gothic UI Light", 20)
        self.label_alto = QLabel("Compila il form di inserimento dell'abbonamento")
        self.label_alto.setFont(self.font_label2)
        self.v_layout.addWidget(self.label_alto)

        # self.v_layout.addSpacing(10)

        self.label_nome = QLabel("Nome:")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.v_layout.addWidget(self.campo_nome)

        self.label_cognome = QLabel("Cognome:")
        self.label_cognome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cognome)

        self.campo_cognome = QLineEdit()
        self.v_layout.addWidget(self.campo_cognome)

        self.label_nato = QLabel("Nato a:")
        self.label_nato.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nato)

        self.campo_nato = QLineEdit()
        self.v_layout.addWidget(self.campo_nato)

        self.label_data = QLabel("Data di nascita (gg/mm/aaaa) :")
        self.label_data.setFont(self.font_label)
        self.v_layout.addWidget(self.label_data)

        self.campo_data = QLineEdit()
        self.v_layout.addWidget(self.campo_data)

        self.label_residenza = QLabel("Residenza (Via e città di residenza) :")
        self.label_residenza.setFont(self.font_label)
        self.v_layout.addWidget(self.label_residenza)

        self.campo_residenza = QLineEdit()
        self.v_layout.addWidget(self.campo_residenza)

        self.label_codicefiscale = QLabel("Codice fiscale (16 caratteri):")
        self.label_codicefiscale.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codicefiscale)

        self.campo_codicefiscale = QLineEdit()
        self.v_layout.addWidget(self.campo_codicefiscale)

        self.label_email = QLabel("Email :")
        self.label_email.setFont(self.font_label)
        self.v_layout.addWidget(self.label_email)

        self.campo_email= QLineEdit()
        self.v_layout.addWidget(self.campo_email)

        self.label_cellulare = QLabel("Cellulare :")
        self.label_cellulare.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cellulare)

        self.campo_cellulare = QLineEdit()
        self.v_layout.addWidget(self.campo_cellulare)

        self.label_struttura = QLabel("Struttura: ")
        self.label_struttura.setFont(self.font_label)
        self.v_layout.addWidget(self.label_struttura)

        self.campo_struttura = QComboBox(self)
        self.campo_struttura.addItem("")
        self.campo_struttura.addItem("Piscina")
        self.campo_struttura.addItem("Palestra")
        self.v_layout.addWidget(self.campo_struttura)

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

        self.label_attivazione_abbonamento = QLabel("Data di attivazione abbonamento (gg/mm/aaaa) :")
        self.label_attivazione_abbonamento.setFont(self.font_label)
        self.v_layout.addWidget(self.label_attivazione_abbonamento)

        self.campo_attivazione_abbonamento = QLineEdit()
        self.v_layout.addWidget(self.campo_attivazione_abbonamento)

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
        self.setWindowTitle("Inserimento Abbonamento")

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 820)
        self.setMaximumSize(781, 820)

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 820))
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
        nato = self.campo_nato.text()
        data = self.campo_data.text()
        codicefiscale = self.campo_codicefiscale.text()
        residenza = self.campo_residenza.text()
        email = self.campo_email.text()
        cellulare = self.campo_cellulare.text()
        struttura = str(self.campo_struttura.currentText())
        tipoabbonamento = str(self.campo_tipoabbonamento.currentText())
        attivazione = self.campo_attivazione_abbonamento.text()


        if nome == "" or cognome == "" or nato == "" or data == "" or codicefiscale == "" or residenza == "" or email == "" or cellulare == "" or tipoabbonamento == "" or attivazione == "":
            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            data = datetime.strptime(data, "%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci la data di nascita nel formato richiesto.", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        try:
            attivazione = datetime.strptime(attivazione, "%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci la data di attivazione nel formato richiesto.", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if len(codicefiscale) < 16:
            QMessageBox.critical(self, "Errore", "Codice fiscale deve avere 16 caratteri", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if len(codicefiscale) > 16:
            QMessageBox.critical(self, "Errore", "Codice fiscale deve avere 16 caratteri", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if not self.controlla_codicefiscale_libero(codicefiscale):
            QMessageBox.critical(self, "Errore", "Il codice fiscale inserito è già stato utilizzato", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        try:
            cellulare = int(self.campo_cellulare.text())

        except:

            QMessageBox.critical(self, "Errore", "Inserisci solo cifre per il numero di cellulare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return


        self.controller.aggiungi_abbonamento(model_gestione_abbonamenti(nome, cognome, nato, data, codicefiscale,residenza, email, cellulare,struttura, tipoabbonamento, attivazione))
        self.controller.save_data()
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))
        QMessageBox.about(self, "Completato", "Inserimento completato")
        self.aggiorna_lista()
        self.close()


    def controlla_codicefiscale_libero(self, codicefiscale):

        for abbonamento in self.controller.get_lista_abbonamenti():
            if abbonamento.codicefiscale == codicefiscale:
                return False
        return True