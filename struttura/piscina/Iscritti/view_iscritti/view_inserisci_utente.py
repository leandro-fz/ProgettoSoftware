from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from struttura.piscina.GestioneIscritti.model_gestione_iscritti.model_gestione_iscritti import model_gestione_iscritti


class view_inserisci_utente(QWidget):

    def __init__(self, controller, aggiorna_lista, parent=None):

        super(view_inserisci_utente, self).__init__(parent)
        self.controller = controller
        self.aggiorna_lista = aggiorna_lista

        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Yu Gothic UI Light", 15)
        self.font_label.setBold(True)


        self.font_label2 = QFont("Yu Gothic UI Light", 20)
        self.label_alto = QLabel("Compila il form di inserimento dell'utente")
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

        self.label_codicefiscale = QLabel("Codice fiscale (16 caratteri):")
        self.label_codicefiscale.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codicefiscale)

        self.campo_codicefiscale = QLineEdit()
        self.v_layout.addWidget(self.campo_codicefiscale)

        self.label_cellulare = QLabel("Cellulare :")
        self.label_cellulare.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cellulare)

        self.campo_cellulare = QLineEdit()
        self.v_layout.addWidget(self.campo_cellulare)

        self.label_certificato = QLabel("Certificato :")
        self.label_certificato.setFont(self.font_label)
        self.v_layout.addWidget(self.label_certificato)

        self.campo_certificato = QLineEdit()
        self.v_layout.addWidget(self.campo_certificato)

        self.label_tipoabbonamento = QLabel("Tipo abbonamento :")
        self.label_tipoabbonamento.setFont(self.font_label)
        self.v_layout.addWidget(self.label_tipoabbonamento)

        self.campo_tipoabbonamento = QLineEdit()
        self.v_layout.addWidget(self.campo_tipoabbonamento)

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
        self.setWindowTitle("Inserimento utente")
        self.resize(300, 400)

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 590)
        self.setMaximumSize(781, 590)

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/sfondonuotosfocato2.jpeg")
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

        nome = self.campo_nome.text()
        cognome = self.campo_cognome.text()
        codicefiscale = self.campo_codicefiscale.text()
        cellulare = self.campo_cellulare.text()
        certificato = self.campo_certificato.text()
        tipoabbonamento = self.campo_tipoabbonamento.text()



        if nome == "" or cognome == "" or codicefiscale == "" or cellulare == "" or certificato == "" or tipoabbonamento == "":
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

        if not self.controlla_codicefiscale_libero(codicefiscale):
            QMessageBox.critical(self, "Errore", "Codice fiscale inserito è già stato utilizzato", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        try:
            cellulare = int(self.campo_cellulare.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per il numero di cellulare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return


        self.controller.aggiungi_utente(model_gestione_iscritti(nome, cognome, codicefiscale,cellulare, certificato,tipoabbonamento))
        self.controller.save_data()

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))
        QMessageBox.about(self, "Completato", "Inserimento completato")
        self.aggiorna_lista()
        self.close()


    def controlla_codicefiscale_libero(self, codicefiscale):

        for utente in self.controller.get_lista_iscritti():
            if utente.codicefiscale == codicefiscale:
                return False
        return True