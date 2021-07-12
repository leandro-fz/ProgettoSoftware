from PyQt5 import QtGui, QtCore

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime


from gestione.cliente.GestioneCertificati.model_gestione_certificati.model_gestione_certificati import \
    model_gestione_certificati
from gestione.cliente.abbonamenti.controller_abbonamenti.controller_abbonamenti import controller_abbonamenti


class view_inserisci_certificati(QWidget):

    def __init__(self, controller, aggiorna_lista, parent=None):

        super(view_inserisci_certificati, self).__init__(parent)
        self.controller = controller
        self.aggiorna_lista = aggiorna_lista


        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Yu Gothic UI Light", 13)
        self.font_label.setBold(True)


        self.font_label2 = QFont("Yu Gothic UI Light",15)
        self.label_alto = QLabel("Compila il form di inserimento del certificato")
        self.label_alto.setFont(self.font_label2)
        self.v_layout.addWidget(self.label_alto)

        # self.v_layout.addSpacing(10)

        # self.label_nome = QLabel("Nome: ")
        # self.label_nome.setFont(self.font_label)
        # self.v_layout.addWidget(self.label_nome)
        #
        # self.campo_nome = QLineEdit()
        # self.v_layout.addWidget(self.campo_nome)
        #
        # self.label_cognome = QLabel("Cognome: ")
        # self.label_cognome.setFont(self.font_label)
        # self.v_layout.addWidget(self.label_cognome)
        #
        # self.campo_cognome = QLineEdit()
        # self.v_layout.addWidget(self.campo_cognome)
        #
        # self.label_nato = QLabel("Nato a: ")
        # self.label_nato.setFont(self.font_label)
        # self.v_layout.addWidget(self.label_nato)
        #
        # self.campo_nato = QLineEdit()
        # self.v_layout.addWidget(self.campo_nato)

        self.label_codicefiscale = QLabel("Codice fiscale (16 caratteri): ")
        self.label_codicefiscale.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codicefiscale)

        self.campo_codicefiscale = QLineEdit()
        self.v_layout.addWidget(self.campo_codicefiscale)

        # self.label_residenza = QLabel("Residenza (Via e città di residenza): ")
        # self.label_residenza.setFont(self.font_label)
        # self.v_layout.addWidget(self.label_residenza)
        #
        # self.campo_residenza = QLineEdit()
        # self.v_layout.addWidget(self.campo_residenza)

        self.label_sportcertificato = QLabel("Sport del certificato:")
        self.label_sportcertificato.setFont(self.font_label)
        self.v_layout.addWidget(self.label_sportcertificato)

        self.campo_sportcertificato= QLineEdit()
        self.v_layout.addWidget(self.campo_sportcertificato)

        self.checkbox_sportcertificato = QCheckBox("Certificato agonistico")
        self.v_layout.addWidget(self.checkbox_sportcertificato)

        self.label_datainizio = QLabel("Data inizio validità certificato (gg/mm/aaaa):")
        self.label_datainizio.setFont(self.font_label)
        self.v_layout.addWidget(self.label_datainizio)

        self.campo_datainizio = QLineEdit()
        self.v_layout.addWidget(self.campo_datainizio)

        self.label_datafine = QLabel("Data scadenza validità certificato (gg/mm/aaaa):")
        self.label_datafine.setFont(self.font_label)
        self.v_layout.addWidget(self.label_datafine)

        self.campo_datafine = QLineEdit()
        self.v_layout.addWidget(self.campo_datafine)

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
        self.setWindowTitle("Inserimento certificato")
        self.resize(300, 400)

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 650)
        self.setMaximumSize(781, 650)

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 660))
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

        # nome = self.campo_nome.text()
        # cognome = self.campo_cognome.text()
        # nato = self.campo_nato.text()
        codicefiscale = self.campo_codicefiscale.text()
        # residenza = self.campo_residenza.text()
        sportcertificato = self.campo_sportcertificato.text()
        datainizio = self.campo_datainizio.text()
        datafine = self.campo_datafine.text()

        if self.checkbox_sportcertificato.isChecked():
            booleancertificato = True
        else:
            booleancertificato = False
        # nome == "" or cognome == "" or nato == "" or residenza == ""
        if codicefiscale == "" or sportcertificato == "" or datainizio == "" or datafine == "":

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


        # if not self.controlla_codicefiscale_libero(codicefiscale):
        #
        #     QMessageBox.critical(self, "Errore", "Codice fiscale inserito è già stato utilizzato", QMessageBox.Ok, QMessageBox.Ok)
        #     return

        if not self.controlla_cf_abbonamento(codicefiscale):

            QMessageBox.critical(self, "Errore", "Codice fiscale non trovato tra gli abbonamenti registrati.\nSe si tratta di un nuovo cliente, registralo prima tra gli abbonamenti", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            datainizio = datetime.strptime(datainizio, "%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci il formato della data richiesto.", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return
        try:
            datafine = datetime.strptime(datafine, "%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci il formato della data richiesto.", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if datafine < datainizio:
            QMessageBox.critical(self, "Errore", "La data di scadenza non può essere precedente alla data di inizio di validità.", QMessageBox.Ok, QMessageBox.Ok)
            return


        self.controller.aggiungi_certificato(model_gestione_certificati(codicefiscale, sportcertificato,booleancertificato, datainizio, datafine))
        self.controller.save_data()

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))
        QMessageBox.about(self, "Completato", "Inserimento completato")
        self.aggiorna_lista()
        self.close()

    def controlla_cf_abbonamento(self, codicefiscale):
        controllerabbonamento = controller_abbonamenti()
        for abbonamento in controllerabbonamento.get_lista_abbonamenti():
            if abbonamento.codicefiscale == codicefiscale:
                return True
        return False

    # def controlla_codicefiscale_libero(self, codicefiscale):
    #
    #     for certificato in self.controller.get_lista_certificati():
    #         if certificato.codicefiscale == codicefiscale:
    #             return False
    #     return True
